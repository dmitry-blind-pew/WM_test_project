import argparse
import csv
from collections import defaultdict
from statistics import median
from tabulate import tabulate


def create_parser() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('--files', nargs='+', help='Список файлов')
    parser.add_argument('--report',  help='Название отчёта')
    args = parser.parse_args()
    return args

def read_csv(data: list) -> dict[str, list]:
    all_data = defaultdict(list)
    for file in data:
        with open(file, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                all_data[row["student"]].append(row["coffee_spent"])
    return all_data

def data_processing(all_data: dict[str, list]) -> list[list]:
    res = [[key,median(val)] for key, val in all_data.items()]
    res.sort(key=lambda x: x[1], reverse=True)
    return res

def main():
    args = create_parser()
    all_data = read_csv(args.files)
    result = data_processing(all_data)

    headers = ["student", "median_coffee"]
    print(tabulate(result, headers=headers, tablefmt='grid'))


if __name__ == "__main__":
    main()
