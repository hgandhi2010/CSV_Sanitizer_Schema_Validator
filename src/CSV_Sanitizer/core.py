"""Core CSV sanitization and schema-validation logic.

Nothing in this file runs on import — everything happens inside sanitize_csv().
"""

import logging
from pathlib import Path

from dateutil import parser


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


def sanitize_csv(input_path, output_path, log_path=None) -> dict:
    """Reads input_path, writes a cleaned CSV to output_path.

    Returns {"rows_written": int, "rows_skipped": int}.
    """
    input_path = Path(input_path)
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    if log_path:
        log_path = Path(log_path)
        log_path.parent.mkdir(parents=True, exist_ok=True)
        logging.basicConfig(
            filename=str(log_path),
            filemode="a",
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
            force=True,
        )

    rows_written = 0
    rows_skipped = 0

    with (
        open(input_path, "r", encoding="utf-8") as file,
        open(output_path, "w", encoding="utf-8") as cleaned_file,
    ):
        row_headings = file.readline()
        header_list = [clean_whitespace(h) for h in row_headings.split(",")]
        expected_length = len(header_list)

        clean_headings = ",".join(header_list) + "\n"
        cleaned_file.write(clean_headings)

        for line in file:
            cleaned_line = line.strip()
            if not cleaned_line:
                continue

            raw_row = cleaned_line.split(",")

            if not validate_row_schema(raw_row, expected_length):
                logging.warning(f"MALFORMED ROW ISOLATED (COLUMN MISMATCH): {raw_row}")
                rows_skipped += 1
                continue

            try:
                cleaned_id = clean_whitespace(raw_row[0])
                cleaned_name = clean_whitespace(raw_row[1])
                cleaned_date = parse_to_iso_8601(raw_row[2])
                cleaned_role = clean_whitespace(raw_row[3])

                clean_line = (
                    f"{cleaned_id},{cleaned_name},{cleaned_date},{cleaned_role}\n"
                )
                cleaned_file.write(clean_line)
                rows_written += 1

            except Exception as parsing_err:
                logging.warning(
                    f"MALFORMED ROW ISOLATED (PARSING ERROR): {raw_row} | Reason: {parsing_err}"
                )
                rows_skipped += 1
                continue

    return {"rows_written": rows_written, "rows_skipped": rows_skipped}
