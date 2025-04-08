import input_employees
from salary import *
from mysql_connect import save_employee_to_db

def print_employees_recursive(employees, index=0):
    names = list(employees.keys())

    if index < len(names):
        print(names[index])
        print_employees_recursive(employees, index + 1)

def main():
    try:
        em = int(input("Введіть кількість співробітників: "))
    except EOFError:
        em = 2
    print(f"Кількість співробітників: {em}")
    employees = input_employees.employee(em)
    print("\nРозрахунок зарплат:")
    for name, data in employees.items():
        total_salary = salarys(data["salary"], data["days_worked"])
        print(f"{name}: {total_salary:.2f} грн")
        save_employee_to_db(name, total_salary, data["days_worked"])

    print("\nСписок співробітників:")
    print_employees_recursive(employees)

if __name__ == "__main__":
    main()
