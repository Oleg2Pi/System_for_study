from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


class Product(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='product'
    )
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    about = models.TextField()
    can_buy = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    start = models.BooleanField(default=False)
    price = models.FloatField(
        default=0.0,
        validators=[MinValueValidator(0.0)]
    )
    min_students = models.IntegerField(default=1)
    max_students = models.IntegerField(default=2)
    lessons = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name


class Lesson(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='lesson'
    )
    name = models.CharField(max_length=250)
    link = models.URLField(max_length=250)

    def __str__(self) -> str:
        return self.name


class Student(models.Model):
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='student'
    )

    def __str__(self) -> str:
        return self.student.username


class Group(models.Model):
    product = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE,
        related_name='group'
    )
    students = models.ManyToManyField(
        Student,
        through="GroupStudents"
    )
    name = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.name
    
    def min_students(self):
        if self.students.all().count() < self.product.min_students:
            return False
        return True
    
    def max_students(self):
        if self.students.all().count() > self.product.max_students:
            return False
        return True
    
    def get_students(self):
        return self.students.all()


class GroupStudents(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE
    )
    