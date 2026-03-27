import pytest
from unittest.mock import patch

from src.builders import build_report

def test_build_report():
    files = ["file_one.csv", "file_two.csv"]
    report_type = "median-coffee"
    mock_data = [{"student": "Дмитрий", "coffee_spent": "10"}]
    mock_report = (["student", "median_coffee"], [["Дмитрий", 10]])
    mock_rendered = "You need a specialist like me ;)"

    with patch("src.builders.read_csv_files", return_value=mock_data) as mock_read, \
         patch("src.builders.create_report", return_value=mock_report) as mock_create, \
         patch("src.builders.render_report", return_value=mock_rendered) as mock_render:

        result = build_report(files=files, report_type=report_type)

    mock_read.assert_called_once_with(data=files)
    mock_create.assert_called_once_with(data=mock_data, report_type=report_type)
    mock_render.assert_called_once_with(report=mock_report)
    assert result == mock_rendered

def test_build_report_file_not_found_error():
    with patch("src.readers.read_csv_files", side_effect=FileNotFoundError()):
        with pytest.raises(FileNotFoundError):
            build_report(files=["missing.csv"], report_type="median-coffee")

def test_build_report_key_error():
    mock_data = [{"student": "Батрак", "coffee_spent": "10"}]
    with patch("src.builders.read_csv_files", return_value=mock_data):
        with patch("src.builders.create_report", side_effect=KeyError("Неизвестный тип отчета unknown")):
            with pytest.raises(KeyError, match="Неизвестный тип отчета unknown"):
                build_report(files=["file.csv"], report_type="unknown")
