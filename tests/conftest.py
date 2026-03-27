import pytest
import os
import subprocess
import sys

from src.readers import read_csv_files

@pytest.fixture
def run_cli():
    def _run(files: list[str], report: str):
        return subprocess.run(
            [sys.executable, "main.py", "--files", *files, "--report", report],
            capture_output=True,
            text=True,
            encoding="utf-8",
            env={**os.environ, "PYTHONIOENCODING": "utf-8"},
            check=False,
        )
    return _run

@pytest.fixture
def empty_csv(tmp_path):
    file = tmp_path / "empty.csv"
    file.write_text("student,date,coffee_spent,sleep_hours,study_hours,mood,exam\n", encoding="utf-8")
    return [str(file)]

@pytest.fixture
def one_row_csv(tmp_path):
    content = (
        "student,date,coffee_spent,sleep_hours,study_hours,mood,exam\n"
        "Алексей Смирнов,2024-06-01,450,4.5,12,норм,Математика\n"
    )
    file = tmp_path / "one_row.csv"
    file.write_text(content, encoding="utf-8")
    return [str(file)]

@pytest.fixture
def standard_csv(tmp_path):
    content = (
        "student,date,coffee_spent,sleep_hours,study_hours,mood,exam\n"
        "Алексей Смирнов,2024-06-01,400,4.5,12,норм,Математика\n"
        "Алексей Смирнов,2024-06-02,500,4.0,14,устал,Математика\n"
        "Дарья Петрова,2024-06-01,200,7.0,6,отл,Математика\n"
    )
    file = tmp_path / "standard.csv"
    file.write_text(content, encoding="utf-8")
    return [str(file)]

@pytest.fixture
def two_files(one_row_csv, standard_csv):
    return one_row_csv + standard_csv

@pytest.fixture
def data_one_row(one_row_csv):
    return read_csv_files(data=one_row_csv)

@pytest.fixture
def data_standard(standard_csv):
    return read_csv_files(data=standard_csv)

@pytest.fixture
def data_empty(empty_csv):
    return read_csv_files(data=empty_csv)
