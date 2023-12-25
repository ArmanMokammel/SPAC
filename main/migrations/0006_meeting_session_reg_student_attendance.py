# Generated by Django 5.0 on 2023-12-24 17:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_reg_student_items'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting_Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speaker_name', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Meeting Session',
            },
        ),
        migrations.CreateModel(
            name='Reg_Student_Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendance', models.BooleanField(default=False)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.meeting_session')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.reg_student')),
            ],
            options={
                'verbose_name': 'Registered Student Attendance',
            },
        ),
    ]
