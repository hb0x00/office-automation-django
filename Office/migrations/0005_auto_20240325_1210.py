# Generated by Django 3.2.12 on 2024-03-25 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Office', '0004_employee_leave_left'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='leave_left',
        ),
        migrations.AddField(
            model_name='leaverecord',
            name='leave_left',
            field=models.IntegerField(default=4, null=True, verbose_name=3),
        ),
    ]
