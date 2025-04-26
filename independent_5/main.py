from input import get_input
from calculation import sin_taylor
from output import display_result
from performance_analysis import performance_test


if __name__ == "__main__":
    x, eps = get_input()
    approx_sin, iterations = sin_taylor(x, eps)
    display_result(x, eps, approx_sin, iterations)

    # Аналіз продуктивності
    x_test_values = [x] * 20
    eps_test_values = [10**(-i) for i in range(1, 21)]
    performance_test(x_test_values, eps_test_values)
