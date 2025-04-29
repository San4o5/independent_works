import json

def print_stats(stats: dict):
    print("+-----------------------------+---------+")
    print("| Показник                    | Значення|")
    print("+-----------------------------+---------+")
    for key, value in stats.items():
        print(f"| {key:<27} | {value:>7} |")
    print("+-----------------------------+---------+")

def save_stats_to_json(stats, filename='output/result.json'):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(stats, file, ensure_ascii=False, indent=4)
        print(f"\nРезультати збережено у файл: {filename}")
    except Exception as e:
        print(f"Помилка під час збереження JSON: {e}")

