# Generated by Django 3.1.6 on 2021-02-16 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0009_auto_20210216_1406'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ride_request',
            old_name='vechile',
            new_name='vehicle',
        ),
    ]
