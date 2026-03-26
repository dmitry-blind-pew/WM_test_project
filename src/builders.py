from __future__ import annotations

from src.readers import read_csv_files
from src.reports import create_report
from src.utils import render_report


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
