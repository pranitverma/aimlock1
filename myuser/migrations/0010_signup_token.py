# Generated by Django 2.0.6 on 2019-07-15 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myuser', '0009_signup_isactive'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='token',
            field=models.CharField(default='', max_length=250),
        ),
    ]
