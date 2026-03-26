from __future__ import annotations
from collections import defaultdict
from statistics import median
from typing import Callable


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
