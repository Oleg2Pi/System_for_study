# Generated by Django 5.0.2 on 2024-02-28 22:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_group_groupstudents_group_students'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='products',
            new_name='product',
        ),
    ]
