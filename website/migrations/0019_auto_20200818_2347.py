# Generated by Django 2.0 on 2020-08-18 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0018_orders'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='cust_id',
            new_name='cust',
        ),
    ]