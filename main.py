from __future__ import annotations
import argparse
import csv
from collections import defaultdict
from statistics import median
from tabulate import tabulate
from typing import Callable


def create_parser() -> argparse.ArgumentParser:
    """
    Создает CLI-парсер с обязательными аргументами "files" и "report".
    Args:
    Returns:
        argparse.ArgumentParser - CLI-парсер.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--files", nargs="+", required=True, help="Список файлов")
    parser.add_argument("--report", required=True, help="Название отчёта")
    return parser

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

def create_report(*, data: list[dict[str, str]], report_type: str) -> tuple[list[str], list[list]]:
    """
    Проверяет наличие отчета в списке имеющихся и если есть - запускает функцию создания отчета.
    Args:
        data: list[dict[str, str]] - данные для формаирования отчета.
        report_type: str - тип отчета.
    Returns:
        tuple[list[str], list[list]] - готовые данные для рендеринга отчета.
    """
    try:
        report = REPORTS_TYPES[report_type](data=data)
    except KeyError:
        raise KeyError(f"Неизвестный тип отчета {report_type}")
    return report

def median_coffee_report(*, data: list[dict[str, str]]) -> tuple[list[str], list[list]]:
    """
    Из полученных данных отбирает только ФИ студента и данные о тратах на кофе. Формирует медианную сумму трат на кофе.
    Сортирует данные по убыванию трат на кофе. Добавляет заголовки для последующего рендеринга.
    Args:
        data: list[dict[str, str]] - данные о студентах.
    Returns:
        tuple[list[str], list[list]] - кортеж, где первый элемент - заголовки для таблицы отчета, а второй - данные для
        таблицы отчета.
    """
    report_dict = defaultdict(list)
    for row in data:
        report_dict[row["student"]].append(int(row["coffee_spent"]))

    final_report = [[key, median(val)] for key, val in report_dict.items()]
    final_report.sort(key=lambda x: x[1], reverse=True)

    headers = ["student", "median_coffee"]
    return headers, final_report


REPORTS_TYPES: dict[str, Callable[..., tuple[list[str], list[list]]]] = {"median-coffee": median_coffee_report}


def render_report(*, report: tuple[list[str], list[list]]) -> str:
    """
    На основе полученных данных рендерит отчет для вывода в терминал.
    Args:
        report: tuple[list[str], list[list]] - кортеж с заголовками и данными для отчета.
    Returns:
        str - готовый для вывода в терминал рендер отчета.
    """
    render = tabulate(report[1], headers=report[0], tablefmt="grid")
    return render

def build_report(*, files: list[str], report_type: str) -> str:
    """
    Основная бизнес-логика. Чтение данных из CSV файлов. Формирование данных для отчета. Создание и рендеринг
    конкретного отчета.
    Args:
        files: list[str] - список с адресами CSV файлов.
        report_type: str - тип отчета, определяющий логику формирования отчета.
    Returns:
        str - готовый для вывода в терминал рендер отчета.
    """
    report_data = read_csv_files(data=files)
    report = create_report(data=report_data, report_type=report_type)
    render_table = render_report(report=report)
    return render_table

def main() -> None:
    """
    Точка входа CLI. Парсит аргументы командной строки, формирует отчёт и выводит его в терминал.
    Args:
    Returns:
        None
    """
    parser = create_parser()
    args = parser.parse_args()
    try:
        render = build_report(files=args.files, report_type=args.report)
        print(render)
    except (FileNotFoundError, KeyError) as error:
        parser.exit(status=1, message=f"{error}\n")


if __name__ == "__main__":
    main()

