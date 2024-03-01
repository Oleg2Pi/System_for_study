from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
# from .serializers import ProductSerializer
from .models import Product, Student, User, Group


# class ProductAPIView(generics.ListAPIView):
#     queryset = Product.objects.filter(can_buy=True)
#     serializer_class = ProductSerializer

class ProductAPIView(APIView):
    def get(self, requests):
        products = Product.objects.filter(can_buy=True)
        count_lessons(products)
        products_values = products.values()
        return Response({
            'products': list(products_values)
        })


def count_lessons(products):
    for product in products:
        if product.lessons != product.lesson.all().count():
            product.lessons = product.lesson.all().count()
            product.save()


class LessonsAPIView(APIView):
    def get(self, requests):
        student = requests.user.student.get()
        group = Group.objects.get(students=student)
        product = group.product
        lessons = list(product.lesson.all().values())
        return Response({'student': student.student.username,
                         'group': group.name,
                         'product': product.name,
                         'lessons': lessons
                         })


def group_distribution(request, id):
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
