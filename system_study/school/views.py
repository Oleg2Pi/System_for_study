from django.shortcuts import render
from .models import Product, Student, User, GroupStudents


def group_distribution(request, id=1):
    product = Product.objects.get(id=id)

    if not request.user.student.exists():
        return 'Not exist a student'
    student = request.user.student.get()
    groups = product.group.all()
    distribution(student, groups)

    if not product.start and students_count(groups, product.min_students):
        rebuild_groups(groups)


def distribution(student, groups):
    for group in groups:
        if group.max_students():
            group.students.add(student.id)


def rebuild_groups(groups):
    students_list, groups_list = parsing(groups)
    while len(students_list) > 0:
        for group in groups_list:
            if len(students_list) == 0:
                break
            group.students.add(students_list.pop(0))


def parsing(groups):
    student_list = []
    group_list = []
    for group in groups:
        group_list.append(group)
        for student in group.students.all():
            student_list.append(student)
        group.students.clear()
    return student_list, group_list


def students_count(groups, min_students):
    students = 0
    min_count_groups = 0
    for group in groups:
        students += group.students.all().count()
        min_count_groups += min_students
    if students >= min_count_groups:
        return True
    return False
