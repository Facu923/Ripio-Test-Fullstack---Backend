# Generated by Django 2.1 on 2018-08-26 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_currencytype'),
    ]

    operations = [
        migrations.AddField(
            model_name='currencytype',
            name='symbol',
            field=models.CharField(default='', max_length=4),
        ),
    ]