import history

#функція отримання кількості книг
def get_books_data():
    books = {}
    try:
        num_books = int(input("Введіть кількість книг: "))
        if num_books <= 0:
            print("Ви не ввели жодної книги.")
            return books
        
        for i in range(num_books):
            title, author, pages = get_book_details(i + 1)
            books[title] = (author, pages)
            history.save_history({title: (author, pages)})

    except ValueError:
        print("Помилка! Введіть коректне число книг.")
    
    return books

#Функція отримання інформації про книгу
def get_book_details(index):
    print(f"\nВведення даних для книги {index}:")
    title = input("Назва книги: ").strip()
    author = input("Автор книги: ").strip()
    pages = get_page_count()
    return title, author, pages

#Функція отримання кількості сторінок
def get_page_count():
    while True:
        try:
            pages = int(input("Кількість сторінок: "))
            if pages <= 0:
                raise ValueError
            return pages
        except ValueError:
            print("Помилка! Введіть коректне число сторінок.")

#Функція підрахунку середньої кількості сторінок
def calculate_avg_pages(books):
    total_pages = 0
    for book in books.values():
        pages = book[1]
        total_pages += pages
    
    avg_pages = total_pages / len(books)
    
    return avg_pages

#Функція отримання книг у яких меньше середньго по сторінкам
def get_books_below_average(books, avg_pages):
    books_below_avg = {}
    for title, (author, pages) in books.items():
        if pages < avg_pages:
            books_below_avg[title] = (author, pages)
    
    return books_below_avg

#Функція для аналізу книги
def analysis_books(books):
    if not books:
        return
    
    avg_pages = calculate_avg_pages(books)
    print(f"\nСередня кількість сторінок у бібліотеці: {avg_pages:.2f}")
    
    fewer_pages_books = get_books_below_average(books, avg_pages)
    
    if fewer_pages_books:
        print("\nКниги, які мають менше сторінок, ніж середнє значення:")
        for title, (author, pages) in fewer_pages_books.items():
            print(f"- {title} (Автор: {author}, Сторінок: {pages})")
    else:
        print("\nУсі книги мають сторінок не менше за середній показник.")
        
#Фукція для перегляду історії
def view_history():
    history_books = history.read_history()
    if history_books:
        print("\nІсторія ввведених книг:")
        for num in history_books:
            print(num.strip())
    else:
        print("Історія порожня")
        
#Функція main
def main():
    print('''
1. Ввести книги
2. Переглянути історію
          ''')
    choice = input("Виберіть дію: ").strip()
    if choice == '1':
        books = get_books_data()
        analysis_books(books)
    elif choice == '2':
        view_history()
    else:
        print("Невірний вибір")

if __name__ == "__main__":
    main()