# Generated by Django 3.2.12 on 2024-05-12 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Office', '0012_auto_20240422_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_leave_apply',
            name='leave_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
