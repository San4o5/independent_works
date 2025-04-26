def get_input():
    try:
        x = float(input("Введіть значення x (у радіанах): "))
        eps = float(input("Введіть точність обчислення eps (позитивне число): "))
        if eps <= 0:
            raise ValueError("Точність має бути додатнім числом.")
        return x, eps
    except ValueError as e:
        print(f"Помилка вводу: {e}")
        return get_input()
