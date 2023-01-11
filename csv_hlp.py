import csv


def read(name):
    with open(f'input/{name}.csv', 'r', encoding="utf-8") as f:
        reader = csv.reader(f)
        return [row for row in reader]


def write(name, header, rows):
    with open(f'output/{name}.csv', 'w', newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)
