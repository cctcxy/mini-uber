# Generated by Django 3.1.6 on 2021-02-16 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0008_auto_20210216_1109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='license_num',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='max_passenger',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='vehicle',
        ),
    ]
