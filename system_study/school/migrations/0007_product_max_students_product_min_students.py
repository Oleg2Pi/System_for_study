# Generated by Django 5.0.2 on 2024-02-28 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0006_rename_products_group_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='max_students',
            field=models.IntegerField(default=2),
        ),
        migrations.AddField(
            model_name='product',
            name='min_students',
            field=models.IntegerField(default=1),
        ),
    ]
