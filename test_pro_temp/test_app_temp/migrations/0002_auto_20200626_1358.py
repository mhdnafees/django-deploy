# Generated by Django 3.0.3 on 2020-06-26 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_app_temp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='Person',
        ),
    ]
