# Generated by Django 2.0 on 2020-08-09 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.EmailField(default='NULL', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='phone',
            field=models.CharField(default='NULL', max_length=10, unique=True),
        ),
    ]
