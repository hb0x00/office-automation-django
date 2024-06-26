# Generated by Django 3.2.12 on 2024-04-21 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Office', '0008_auto_20240421_0623'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_employee',
            name='contact_number',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
        migrations.AddField(
            model_name='tbl_employee',
            name='designation',
            field=models.CharField(blank=True, choices=[('Senior lecturer', 'Senior lecturer'), ('lecturer', 'lecturer'), ('HOD', 'HOD')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tbl_employee',
            name='email_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
