# Generated by Django 2.0.6 on 2019-07-09 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myuser', '0004_signup_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='mobile',
            field=models.BigIntegerField(null=True, unique=True),
        ),
    ]
