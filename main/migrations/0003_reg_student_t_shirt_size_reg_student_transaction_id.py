# Generated by Django 5.0 on 2023-12-23 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_reg_student_department_reg_student_picture_link_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reg_student',
            name='t_shirt_size',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='reg_student',
            name='transaction_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]