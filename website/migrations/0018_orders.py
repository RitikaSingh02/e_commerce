# Generated by Django 2.0 on 2020-08-18 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0017_auto_20200818_2330'),
    ]

    operations = [
        migrations.CreateModel(
            name='orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(default='NULL', max_length=200)),
                ('cust_mail', models.CharField(default='NULL', max_length=200)),
                ('checksum', models.CharField(default='NULL', max_length=250)),
                ('trans_id', models.CharField(default='NULL', max_length=250)),
                ('status', models.CharField(default='pending', max_length=250)),
                ('cust_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.users')),
            ],
        ),
    ]
