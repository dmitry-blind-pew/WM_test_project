import pytest
from unittest.mock import patch, MagicMock
from src.reports import create_report, REPORTS_TYPES


def test_create_report_calls_correct_function(data_standard):
    mock_report_func = MagicMock(return_value=(["mock_header"], [["mock_data"]]))
    with patch.dict(REPORTS_TYPES, {"median-coffee": mock_report_func}):
        result = create_report(data=data_standard, report_type="median-coffee")

    mock_report_func.assert_called_once_with(data=data_standard)
    assert result == (["mock_header"], [["mock_data"]])


def test_create_report_unknown_type():
    with pytest.raises(KeyError, match="Неизвестный тип отчета unknown"):
        create_report(data=[], report_type="unknown")
