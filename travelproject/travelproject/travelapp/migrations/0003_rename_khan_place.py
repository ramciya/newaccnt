# Generated by Django 4.1.6 on 2023-02-12 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0002_rename_place_khan'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Khan',
            new_name='Place',
        ),
    ]
