# Generated by Django 3.2.12 on 2024-04-22 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Office', '0011_auto_20240422_1413'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tbl_employee',
            old_name='user',
            new_name='employee',
        ),
        migrations.AlterField(
            model_name='tbl_leave_apply',
            name='leave_type',
            field=models.CharField(blank=True, choices=[('1', 'Sick Leave'), ('2', 'Casual Leave'), ('3', 'Earned Leave')], max_length=100, null=True),
        ),
    ]
