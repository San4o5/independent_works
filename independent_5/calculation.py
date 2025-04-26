import math

def sin_taylor(x, eps):
    term = x 
    sum_ = x  
    n = 1
    iterations = 1

    while abs(term) >= eps:
        term *= -x * x / ((2 * n) * (2 * n + 1))
        sum_ += term
        n += 1
        iterations += 1

    return sum_, iterations