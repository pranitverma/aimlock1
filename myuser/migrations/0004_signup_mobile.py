# Generated by Django 2.0.6 on 2019-07-09 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myuser', '0003_signup_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='mobile',
            field=models.BigIntegerField(null=True),
        ),
    ]
