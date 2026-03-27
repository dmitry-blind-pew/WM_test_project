import pytest

from src.readers import read_csv_files
from tests.test_data.expected_results import EMPTY_EXPECTED, ONE_ROW_EXPECTED, STANDARD_EXPECTED, TWO_FILES_EXPECTED


@pytest.mark.parametrize(
    "fixture_name, expected",
    [
        ("empty_csv", EMPTY_EXPECTED),
        ("one_row_csv", ONE_ROW_EXPECTED),
        ("standard_csv", STANDARD_EXPECTED),
        ("two_files", TWO_FILES_EXPECTED),
    ],
)
def test_read_csv_files(fixture_name, expected, request):
    file_paths = request.getfixturevalue(fixture_name)
    result = read_csv_files(data=file_paths)
    assert result == expected


def test_read_csv_files_empty_list():
    assert read_csv_files(data=[]) == []


def test_read_csv_files_wrong_path():
    with pytest.raises(FileNotFoundError):
        read_csv_files(data=["tests/test_data/wrong.csv"])


def test_read_csv_files_valid_and_wrong_path(one_row_csv):
    mixed_paths = one_row_csv + ["tests/test_data/wrong.csv"]
    with pytest.raises(FileNotFoundError, match="wrong.csv"):
        read_csv_files(data=mixed_paths)