def group_students_dict(students):
    groups = {}
    for s in students:
        groups.setdefault(s['group'], []).append(s['name'])
    return groups

def honors_groups(students):
    return {
        s['group']
        for s in students
        if all(grade >= 90 for grade in s['grades'])
    }
