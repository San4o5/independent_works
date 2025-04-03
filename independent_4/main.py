import input_employees
import salary

def print_employees_recursive(employees, index=0):
    names = list(employees.keys())

    if index < len(names):
        print(names[index])
        print_employees_recursive(employees, index + 1)

def main():
    em = input_employees.number_employee()
    employees = input_employees.employee(em)
    print("\nРозрахунок зарплат:")
    for name, data in employees.items():
        total_salary = salary.salarys(data["salary"], data["days_worked"])
        print(f"{name}: {total_salary:.2f} грн")

    print("\nСписок співробітників:")
    print_employees_recursive(employees)

if __name__ == "__main__":
    main()
