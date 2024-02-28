from django.contrib import admin
from .models import Product, Lesson, Student, Group, GroupStudents


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'created', 'price']
    list_filter = ['name', 'created', 'price', 'author']
    search_fields = ['name', 'body']
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['-created']

@admin.register(Group)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'product']


admin.site.register(Lesson)
admin.site.register(Student)
# admin.site.register(Group)
admin.site.register(GroupStudents)
