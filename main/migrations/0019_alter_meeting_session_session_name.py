# Generated by Django 5.0 on 2023-12-25 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_meeting_session_session_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting_session',
            name='session_name',
            field=models.CharField(max_length=150),
        ),
    ]
