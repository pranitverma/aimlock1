# Generated by Django 2.0.6 on 2019-07-09 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myuser', '0005_auto_20190709_1234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='address',
        ),
    ]