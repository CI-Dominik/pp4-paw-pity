# Generated by Django 5.1.3 on 2024-12-11 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0004_rename_is_found_animal_is_approachable_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='is_approachable',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]