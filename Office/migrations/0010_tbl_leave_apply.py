# Generated by Django 3.2.12 on 2024-04-21 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Office', '0009_auto_20240421_0643'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_leave_apply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('month', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=100)),
                ('number_of_leave_taken', models.IntegerField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Office.tbl_employee')),
                ('leave_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Office.tbl_leave_type')),
            ],
            options={
                'verbose_name': 'tbl_leave_apply',
                'verbose_name_plural': 'tbl_leave_apply',
            },
        ),
    ]
