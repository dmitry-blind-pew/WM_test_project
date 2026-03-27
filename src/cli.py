from __future__ import annotations
import argparse

from src.builders import build_report


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
