from __future__ import annotations
from tabulate import tabulate


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
