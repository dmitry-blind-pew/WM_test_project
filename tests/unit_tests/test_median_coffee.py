import pytest
from src.reports import median_coffee_report
from tests.test_data.expected_results import ONE_ROW_MEDIAN_EXPECTED, STANDARD_MEDIAN_EXPECTED, EMPTY_EXPECTED

@pytest.mark.parametrize(
    "data_fixture_name, expected",
    [
        ("data_one_row", ONE_ROW_MEDIAN_EXPECTED),
        ("data_standard", STANDARD_MEDIAN_EXPECTED),
        ("data_empty", EMPTY_EXPECTED),
    ]
)
def test_median_coffee_report(data_fixture_name, expected, request):
    data = request.getfixturevalue(data_fixture_name)
    headers, result = median_coffee_report(data=data)
    assert headers == ["student", "median_coffee"]
    assert result == expected
