import pytest
from src.main import clean_whitespace, parse_to_iso_8601, validate_row_schema


# ==============================================================================
# 1. TESTING WHITESPACE SANITIZATION
# ==============================================================================
def test_clean_whitespace_strips_hidden_characters():
    """Ensure leading, trailing, and hidden whitespace tabs are cleanly stripped."""
    dirty_input = "  Hemin Gandhi\t "
    expected_output = "Hemin Gandhi"
    assert clean_whitespace(dirty_input) == expected_output


# ==============================================================================
# 2. TESTING DYNAMIC DATE TIMELINE PARSING
# ==============================================================================
@pytest.mark.parametrize(
    "dirty_date, expected_iso",
    [
        ("07/11/2026", "2026-07-11"),  # US Standard
        ("11-07-2026", "2026-07-11"),  # European Standard
        ("2026/07/11", "2026-07-11"),  # Alternative Slash Standard
        ("2026-07-11 09:25:00", "2026-07-11T09:25:00"),  # Timestamp Standard
    ],
)
def test_parse_to_iso_8601_handles_mixed_formats(dirty_date, expected_iso):
    """Ensure python-dateutil correctly standardizes dynamic enterprise date expressions."""
    assert parse_to_iso_8601(dirty_date) == expected_iso


# ==============================================================================
# 3. TESTING SCHEMA & COLUMN BOUNDARIES
# ==============================================================================
def test_validate_row_schema_detects_malformed_columns():
    """Ensure rows that deviate from the expected column length trigger an error flag."""
    expected_header_length = 4  # e.g., [id, name, date, role]

    good_row = ["1", "Hemin", "2026-07-11", "Admin"]
    bad_row_short = ["2", "Corrupt Line", "2026-07-11"]  # Missing role
    bad_row_long = [
        "3",
        "Exploit",
        "Comma, Break",
        "2026-07-11",
        "User",
    ]  # Too many items

    # A good row should validate successfully (True)
    assert validate_row_schema(good_row, expected_header_length) is True

    # Broken asymmetric rows should fail validation (False) instead of throwing an index crash
    assert validate_row_schema(bad_row_short, expected_header_length) is False
    assert validate_row_schema(bad_row_long, expected_header_length) is False
