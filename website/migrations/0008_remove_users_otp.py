# Generated by Django 2.0 on 2020-08-11 03:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20200811_0846'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='otp',
        ),
    ]
