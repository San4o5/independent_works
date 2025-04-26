import math

def sin_taylor(x, eps):
    term = x #перше доданок у ряді
    sum_ = x  
    n = 1 #лічильник для формули факторіалів
    iterations = 1 #кількість ітерацій

    while abs(term) >= eps:
        term *= -x * x / ((2 * n) * (2 * n + 1))
        sum_ += term
        n += 1
        iterations += 1

    return sum_, iterations