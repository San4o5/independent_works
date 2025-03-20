import os
# Функція збереження історії у окремий файл
def save_history(books, folder="History", filename="books_history.txt"):
    #шлях до папки
    folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), folder)
    
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    #повний шлях до файлу
    file_path = os.path.join(folder_path, filename)
    
    with open(file_path, "a", encoding="utf-8") as file:
        for title, (author, pages) in books.items():
            file.write(f"Назва: {title}, Автор: {author}, Кількість сторінок: {pages}\n")

#Функція для перегляду історії з файлу
def read_history(folder="History", filename="books_history.txt"):
    #шлях до папки
    folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), folder)
    #шлях до файлу
    file_path = os.path.join(folder_path, filename)
    
    if not os.path.exists(file_path):
        print("Історії не найдено")
        return []

    with open(file_path, "r", encoding="utf-8") as file:
        history = file.readlines()

    return history
