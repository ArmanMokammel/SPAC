# Generated by Django 5.0 on 2023-12-23 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_reg_student_t_shirt_size_reg_student_transaction_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reg_student',
            name='ieee_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
