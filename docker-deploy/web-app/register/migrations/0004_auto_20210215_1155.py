# Generated by Django 3.1.6 on 2021-02-15 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_role_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride_request',
            name='vechile',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.DeleteModel(
            name='Role',
        ),
    ]