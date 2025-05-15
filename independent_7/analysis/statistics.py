import numpy as np

def calculate_student_averages(students):
    return {s['name']: float(np.mean(s['grades'])) for s in students}

def calculate_group_averages(students):
    groups = {}
    for s in students:
        g = s['group']
        groups.setdefault(g, []).append(np.mean(s['grades']))
    return {g: float(np.mean(vals)) for g, vals in groups.items()}

def get_above_average_students(students, group_averages):
    return [
        s['name']
        for s in students
        if np.mean(s['grades']) > group_averages[s['group']]
    ]
