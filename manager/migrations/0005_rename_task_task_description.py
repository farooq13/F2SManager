# Generated by Django 5.1.7 on 2025-03-29 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0004_alter_task_priority'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='task',
            new_name='description',
        ),
    ]
