import csv

def read_csv(filepath):
    with open(filepath, encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)  # пропустити заголовок
        for row in reader:
            yield row
