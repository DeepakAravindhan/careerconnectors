# Generated by Django 5.1.4 on 2025-02-28 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('c2c', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='email',
            field=models.EmailField(max_length=30, unique=True),
        ),
    ]
