# Generated by Django 5.0.6 on 2024-06-09 03:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_assigment'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Assigment',
            new_name='Assignment',
        ),
    ]
