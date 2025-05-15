from cli.args import parse_args
from reader.file_reader import read_csv
from parser.student_parser import parse_students
from analysis.statistics import (
    calculate_student_averages,
    calculate_group_averages,
    get_above_average_students,
)
from analysis.containers import group_students_dict, honors_groups
from reporting.charts import plot_group_averages, plot_subject_boxplot
import json

def main():
    args = parse_args()

    # Генератор: построкове читання CSV
    rows = read_csv(args.file)

    # Парсинг у структури
    students = parse_students(rows, args.group)

    # NumPy: аналітика
    student_avgs = calculate_student_averages(students)
    group_avgs = calculate_group_averages(students)
    above_avg = get_above_average_students(students, group_avgs)

    # Контейнери
    groups = group_students_dict(students)
    honor_set = honors_groups(students)

    # Візуалізація
    plot_group_averages(group_avgs)
    plot_subject_boxplot(students)

    # Експорт
    if args.export:
        enriched = [
            {**s, 'average': student_avgs[s['name']]} for s in students
        ]
        with open(args.export, 'w', encoding='utf-8') as f:
            json.dump(enriched, f, indent=4, ensure_ascii=False)


    # Демонстрація результатів
    print(f"\nСередній бал по студентах: {student_avgs}")
    print(f"Середній бал по групах: {group_avgs}")
    print(f"Студенти вище середнього: {above_avg}")
    print(f"Групи з відмінниками: {honor_set}")

if __name__ == "__main__":
    main()
