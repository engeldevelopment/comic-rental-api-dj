# Generated by Django 3.1.7 on 2021-03-19 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comicsapp', '0002_rent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rent',
            name='finished_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='rent',
            name='rented_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]