# Generated by Django 5.0.2 on 2024-02-28 22:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_alter_product_author_lesson_student'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lesson',
            old_name='product_lesson',
            new_name='product',
        ),
    ]
