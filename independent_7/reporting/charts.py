import matplotlib.pyplot as plt
import numpy as np

def plot_group_averages(group_averages):
    groups = list(group_averages.keys())
    scores = list(group_averages.values())
    plt.figure(figsize=(8, 5))
    plt.bar(groups, scores, color='skyblue')
    plt.title('Середній бал по групах')
    plt.xlabel('Група')
    plt.ylabel('Середній бал')
    plt.tight_layout()
    plt.show()

def plot_subject_boxplot(students):
    subjects = list(zip(*[s['grades'] for s in students]))
    plt.figure(figsize=(8, 5))
    plt.boxplot(subjects, labels=["Math", "Physics", "Python"])
    plt.title('Розподіл оцінок по предметах')
    plt.ylabel('Оцінка')
    plt.tight_layout()
    plt.show()
