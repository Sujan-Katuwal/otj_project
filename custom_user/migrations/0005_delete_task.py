# Generated by Django 5.1.3 on 2024-11-20 03:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0004_alter_task_due_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Task',
        ),
    ]
