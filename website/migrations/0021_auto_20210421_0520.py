# Generated by Django 2.2.14 on 2021-04-21 05:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0020_orders_product_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='otp_table',
        ),
        migrations.DeleteModel(
            name='verified_emails',
        ),
    ]