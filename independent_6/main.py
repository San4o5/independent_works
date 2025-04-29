import sys #обробка аргументів командного рядка 
from parser.tokenizer import tokenize
from analysis.word_stats import *
from analysis.digit_stats import *
from output.printer import print_stats

def read_input():
    #Зчитування вхідних даних з командного рядка або файлу.
    if len(sys.argv) < 2:
        raise RuntimeError("Введіть текст або файл!")
    
    #sys.argv[0] - це ім'я файлу
    #sys.argv[1] - це перший аргумент
    if sys.argv[1] == '-f':
        try:
            filename = sys.argv[2]
            with open(filename, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            raise RuntimeError(f"Файл {filename} не знайдено!")
        except Exception as e:
            raise RuntimeError(f"Помилка читання файлу: {e}")
    else:
        return ' '.join(sys.argv[1:])  # Об'єднує всі аргументи після команди

def main():
    text = read_input()
    tokens = tokenize(text)

    stats = {
        "Кількість слів": count_words(tokens),
        "Слів довжини 3": count_words_len(tokens, 3),
        "Унікальних слів": count_unique_words(tokens),
        "Починаються з великої": count_titlecase_words(tokens),
        "Чисел": count_digits(tokens),
        "Кількість знакозмін": alternation_count(tokens)
    }

    print_stats(stats)

if __name__ == "__main__":
    main()
