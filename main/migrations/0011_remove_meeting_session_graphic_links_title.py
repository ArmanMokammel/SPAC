# Generated by Django 5.0 on 2023-12-25 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_remove_meeting_session_graphics_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meeting_session_graphic_links',
            name='title',
        ),
    ]