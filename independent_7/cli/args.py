import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Аналіз результатів студентів")
    parser.add_argument('--file', required=True, help='Шлях до CSV-файлу')
    parser.add_argument('--group', help='Фільтр по групі (необов’язково)')
    parser.add_argument('--export', help='Файл для експорту JSON')
    return parser.parse_args()
