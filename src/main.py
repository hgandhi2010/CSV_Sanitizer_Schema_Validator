import os
import logging
from dateutil import parser
from pathlib import Path
from dotenv import load_dotenv

# 1. Dynamically locate the main directory (one level up from main.py)
BASE_DIR = Path(__file__).resolve().parent.parent

# 2. Tell load_dotenv exactly where the .env file lives and force an override
load_dotenv(dotenv_path=BASE_DIR / ".env", override=True)


def clean_whitespace(dirty_input: str) -> str:
    if not isinstance(dirty_input, str):
        return ""
    cleaned_string = dirty_input.replace("\ufeff", "")
    return cleaned_string.strip()


def parse_to_iso_8601(date_str: str) -> str:
    parsed_date = parser.parse(date_str)
    clean_date = parsed_date.date().isoformat()
    return clean_date


def validate_row_schema(row: list, expected_length: int) -> bool:
    return len(row) == expected_length


def get_enterprise_path():
    """Retrieves and validates system directories from environment variables."""
    input_path_raw = os.getenv("TARGET_INPUT_DIR")
    output_path_raw = os.getenv("CLEAN_OUTPUT_DIR")
    log_path_raw = os.getenv("ERROR_LOG_PATH")

    if not input_path_raw or not output_path_raw or not log_path_raw:
        raise EnvironmentError(
            "CRITICAL CONFIGURATION ERROR: Environment paths are not set up properly!"
        )

    input_dir = Path(input_path_raw)
    output_dir = Path(output_path_raw)
    log_dir = Path(log_path_raw)
    log_dir.parent.mkdir(parents=True, exist_ok=True)

    logging.basicConfig(
        filename=str(log_dir),
        filemode="a",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        force=True,
    )

    return input_dir, output_dir, log_dir


def path_Validation():
    try:
        source_dir, destination_dir, logging_dir = get_enterprise_path()
        logging.info(
            f"{source_dir}, {destination_dir}, {logging_dir} located successfully, input file is ready for cleanup"
        )
    except EnvironmentError as env_err:
        logging.warning(
            f"CONFIGURATION ERROR: Source files could not be found: {env_err}"
        )
        return None
    except Exception as e:
        logging.error(f"SYSTEM FAILURE: Unexpected error occurred: {e}")
        return None

    return source_dir, destination_dir, logging_dir


# --- EXECUTION PIPELINE ---
source_dir, destination_dir, logging_dir = path_Validation()

if source_dir and destination_dir:
    with (
        open(source_dir / "dirty_data.csv", "r", encoding="utf-8") as file,
        open(destination_dir / "clean_data.csv", "w", encoding="utf-8") as cleaned_file,
    ):
        row_headings = file.readline()
        header_list = [clean_whitespace(h) for h in row_headings.split(",")]
        expected_length = len(header_list)

        # Standardized header entry
        clean_headings = ",".join(header_list) + "\n"
        cleaned_file.write(clean_headings)

        for line in file:
            cleaned_line = line.strip()
            if not cleaned_line:
                continue

            raw_row = cleaned_line.split(",")

            # 1. Structural schema validation
            if not validate_row_schema(raw_row, expected_length):
                logging.warning(f"MALFORMED ROW ISOLATED (COLUMN MISMATCH): {raw_row}")
                continue

            # 2. Field processing block wrapped defensively
            try:
                cleaned_id = clean_whitespace(raw_row[0])
                cleaned_name = clean_whitespace(raw_row[1])
                cleaned_date = parse_to_iso_8601(raw_row[2])
                cleaned_role = clean_whitespace(raw_row[3])

                # Standard CSV structure without padding spaces
                clean_line = (
                    f"{cleaned_id},{cleaned_name},{cleaned_date},{cleaned_role}\n"
                )
                cleaned_file.write(clean_line)

            except Exception as parsing_err:
                logging.warning(
                    f"MALFORMED ROW ISOLATED (PARSING ERROR): {raw_row} | Reason: {parsing_err}"
                )
                continue
