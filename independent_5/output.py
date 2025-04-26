import math

def display_result(x, eps, approx_sin, iterations):
    print(f"\nОбчислення sin({x}) з точністю {eps}:")
    print(f"Приблизне значення: {approx_sin}")
    print(f"Реальне значення: {math.sin(x)}")
    print(f"Кількість ітерацій: {iterations}")