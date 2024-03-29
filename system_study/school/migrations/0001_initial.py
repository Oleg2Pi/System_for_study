# Generated by Django 5.0.2 on 2024-02-28 21:33

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('price', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='study_product', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
