import json

# Функція для виведення статистики у вигляді таблиці
def print_stats(stats: dict):
    print("+-----------------------------+---------+")
    print("| Показник                    | Значення|")
    print("+-----------------------------+---------+")
    for key, value in stats.items():
        print(f"| {key:<27} | {value:>7} |")
    print("+-----------------------------+---------+")

# Функція для збереження статистики у JSON форматі
def save_stats_to_json(stats, filename='output/result.json'):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            # Записуємо статистику у JSON форматі з відступами для зручного читання
            json.dump(stats, file, ensure_ascii=False, indent=4)
            
        print(f"\nРезультати збережено у файл: {filename}")
    except Exception as e:
        print(f"Помилка під час збереження JSON: {e}")

