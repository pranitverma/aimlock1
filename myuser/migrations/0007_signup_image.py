# Generated by Django 2.0.6 on 2019-07-12 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myuser', '0006_remove_signup_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='image',
            field=models.CharField(default='', max_length=250, null=True),
        ),
    ]
