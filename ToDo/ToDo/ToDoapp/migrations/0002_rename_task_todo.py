# Generated by Django 4.2.8 on 2023-12-28 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Task',
            new_name='ToDo',
        ),
    ]
