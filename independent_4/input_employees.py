
def number_employee():
    while True:
        try:
            em = int(input("Введіть кількість співробітників: "))
            if em < 0:
                print("Кількість співробітників не може бути від'ємною. Спробуйте ще раз.")
                continue
            return em
        except ValueError:
            print("Помилка! Введіть ціле число.")


def employee(em):
    employees = {}
    for i in range(em):
        print(f"\nВведіть дані для співробітника {i + 1}:")
        name = input("Введіть ім'я співробітника: ")
        
        while True:
            try:
                salary = float(input("Введіть заробітну плату за місяць: "))
                break
            except ValueError:
                print("Помилка! Введіть коректне число.")

        while True:
            try:
                days = int(input("Введіть кількість відпрацьованих днів: "))
                if days < 0 or days > 30:
                    print("Кількість днів має бути в межах 0-30. Спробуйте ще раз.")
                    continue
                break
            except ValueError:
                print("Помилка! Введіть ціле число.")

        employees[name] = {"salary": salary, "days_worked": days}
    
    return employees
