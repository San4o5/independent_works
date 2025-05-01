import sys #обробка аргументів командного рядка 
import os 
from parser.tokenizer import tokenize
from analysis.word_stats import *
from analysis.digit_stats import *
from output.printer import print_stats
from output.printer import save_stats_to_json
from PyPDF2 import PdfReader
#from cloud.storage import upload_file_to_bucket
#from cloud.speech_to_text import transcribe_audio


def read_input():
    #Зчитування вхідних даних з командного рядка або файлу.
    if len(sys.argv) < 2:
        raise RuntimeError("Введіть текст або файл!")
    
    #sys.argv[0] - це ім'я файлу
    #sys.argv[1] - це перший аргумент
    if sys.argv[1] == '-f':
        filename = sys.argv[2]
        ext = os.path.splitext(filename)[-1].lower()
        
        if ext == '.pdf':
            try:
                with open(filename, 'rb') as file:
                    reader = PdfReader(file)
                    text = ""
                    for page in reader.pages:
                        text += page.extract_text()
                    return text
            except Exception:
                raise RuntimeError(f"Помилка читання PDF: {Exception}")

        else:
            try:
                with open(filename, 'r', encoding='utf-8') as file:
                    return file.read()
            except FileNotFoundError:
                raise RuntimeError(f"Файл {filename} не знайдено!")
            except Exception as e:
                raise RuntimeError(f"Помилка читання файлу: {e}")
    else:
        return ' '.join(sys.argv[1:])  # Об'єднує всі аргументи після команди

def main():
    filename = None
    if "-f" in sys.argv:
        filename = sys.argv[sys.argv.index("-f") + 1]
    
    
    # Отримуємо текст із файлу або аргументів командного рядка
    text = read_input()
    
    # Токенізація тексту
    tokens = tokenize(text)

    # Статистика
    stats = {
        "Кількість слів": count_words(tokens),
        "Слів довжини 3": count_words_len(tokens, 3),
        "Унікальних слів": count_unique_words(tokens),
        "Починаються з великої": count_titlecase_words(tokens),
        "Чисел": count_digits(tokens),
        "Кількість знакозмін": alternation_count(tokens)
    }
    
    # Друкуємо статистику
    print_stats(stats)
    
    if "--save" in sys.argv:
        save_stats_to_json(stats)

    if "--upload" in sys.argv:
        from cloud.storage import upload_file_to_bucket
        upload_file_to_bucket("text-analyzer-sedziro-20250428", filename, os.path.basename(filename))
        
    if "--audio" in sys.argv:
        from cloud.speech_to_text import transcribe_audio
        try:
            audio_path = sys.argv[sys.argv.index("--audio") + 1]
            text = transcribe_audio(audio_path)
            
            with open("output/transcript.txt", "w", encoding="utf-8") as f:
                f.write(text)
            print("Транскрипцію збережено у файл: output/transcript.txt")
        except IndexError:
            print(f"Помилка: після '--audio' не вказано шлях до аудіофайлу!")
            return

if __name__ == "__main__":
    main()
