# Generated by Django 3.2.12 on 2024-03-25 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Office', '0003_attendancerecord_leaverecord'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='leave_left',
            field=models.IntegerField(default=3, null=True),
        ),
    ]
