from __future__ import annotations
import csv


def read_csv_files(*, data: list[str]) -> list[dict[str, str]]:
    """
    Читает строки из всех полученных CSV-файлов и упаковывает общий список.
    Args:
        data: list[str] - список с адресами CSV файлов.
    Returns:
        list[dict[str, str] - список словарей, гдек каждый словарь - строка CSV-файла.
    """
    report_data = []
    for file in data:
        try:
            with open(file, newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                report_data.extend(reader)
        except FileNotFoundError:
            raise FileNotFoundError(f"Файл {file} не существует или указан неверный путь.")
    return report_data
