# Generated by Django 5.1.3 on 2024-12-11 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_alter_comment_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='is_approved',
        ),
    ]
