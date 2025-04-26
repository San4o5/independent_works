import time
import matplotlib.pyplot as plt
from calculation import sin_taylor

def performance_test(x_values, eps_values):
    iteration_counts = []
    times = []

    

    for x, eps in zip(x_values, eps_values):
        start_time = time.perf_counter()
        _, iterations = sin_taylor(x, eps)
        end_time = time.perf_counter()

        iteration_counts.append(iterations)
        times.append(end_time - start_time)

    plt.figure(figsize=(8,6))
    plt.plot(iteration_counts, times, marker='o')
    plt.title("Залежність часу виконання від кількості ітерацій")
    plt.xlabel("Кількість ітерацій")
    plt.ylabel("Час виконання (сек)")
    plt.grid(True)
    plt.show()
