"""Command-line entry point for csv-sanitizer."""

import argparse
import os
import sys
from pathlib import Path

from dotenv import load_dotenv

from .core import sanitize_csv


def get_enterprise_paths():
    """Legacy .env fallback: TARGET_INPUT_DIR / CLEAN_OUTPUT_DIR / ERROR_LOG_PATH."""
    BASE_DIR = Path(__file__).resolve().parent.parent.parent
    load_dotenv(dotenv_path=BASE_DIR / ".env", override=True)

    input_dir = os.getenv("TARGET_INPUT_DIR")
    output_dir = os.getenv("CLEAN_OUTPUT_DIR")
    log_path = os.getenv("ERROR_LOG_PATH")

    if not input_dir or not output_dir:
        raise EnvironmentError(
            "TARGET_INPUT_DIR and CLEAN_OUTPUT_DIR must be set in .env"
        )

    input_csv = Path(input_dir) / "dirty_data.csv"
    output_csv = Path(output_dir) / "clean_data.csv"
    return str(input_csv), str(output_csv), log_path


def build_parser():
    parser = argparse.ArgumentParser(
        prog="csv-sanitizer",
        description="Stream, sanitize, and schema-validate a messy CSV file.",
    )
    parser.add_argument(
        "input", nargs="?", default=None, help="Path to the dirty input CSV file"
    )
    parser.add_argument(
        "output", nargs="?", default=None, help="Path to write the cleaned CSV file"
    )
    parser.add_argument(
        "--log",
        dest="log_path",
        default=None,
        help="Optional path for a log of skipped rows",
    )
    return parser


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    input_path, output_path, log_path = args.input, args.output, args.log_path

    if not input_path or not output_path:
        try:
            input_path, output_path, env_log_path = get_enterprise_paths()
            log_path = log_path or env_log_path
        except EnvironmentError as e:
            print(
                f"Error: no input/output given, and no .env fallback found.\n  {e}",
                file=sys.stderr,
            )
            return 1

    try:
        stats = sanitize_csv(input_path, output_path, log_path)
    except FileNotFoundError:
        print(f"Error: input file not found: {input_path}", file=sys.stderr)
        return 1

    print(
        f"Done. {stats['rows_written']} rows written, {stats['rows_skipped']} rows skipped."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
