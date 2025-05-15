def parse_students(rows, group_filter=None):
    students = []
    for row in rows:
        name, group, *grades = row
        if group_filter and group != group_filter:
            continue
        students.append({
            'name': name,
            'group': group,
            'grades': list(map(int, grades))
        })
    return students
