import argparse
import csv
from collections import defaultdict
from statistics import median
from tabulate import tabulate


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument('--files', nargs='+', help='Список файлов')
    parser.add_argument('--report',  help='Название отчёта')
    return parser

def read_csv_files(*, data: list) -> list[dict]:
    report_data = []
    for file in data:
        with open(file, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            report_data.extend(reader)
    return report_data

def create_report(*, data: list[dict], report_type: str) -> tuple[list[str], list[list]]:
    report = REPORTS_TYPES[report_type](data=data)
    return report

def median_coffee_report(*, data: list[dict]) -> tuple[list[str], list[list]]:
    report_dict = defaultdict(list)
    for row in data:
        report_dict[row["student"]].append(int(row["coffee_spent"]))

    final_report = [[key, median(val)] for key, val in report_dict.items()]
    final_report.sort(key=lambda x: x[1], reverse=True)

    headers = ["student", "median_coffee"]
    return (headers, final_report)


REPORTS_TYPES = {"median-coffee": median_coffee_report}


def render_report(*, report: tuple[list[str], list[list]]) -> str:
    render = tabulate(report[1], headers=report[0], tablefmt="grid")
    return render

def main() -> None:
    parser = create_parser()
    args = parser.parse_args()
    report_data = read_csv_files(data=args.files)
    report = create_report(data=report_data, report_type=args.report)
    render = render_report(report=report)
    print(render)


if __name__ == "__main__":
    main()

