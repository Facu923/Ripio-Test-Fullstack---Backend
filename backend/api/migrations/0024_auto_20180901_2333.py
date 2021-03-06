# Generated by Django 2.1 on 2018-09-02 02:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_auto_20180901_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfer',
            name='accountFrom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accountFrom', to='api.Account'),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='accountTo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accountTo', to='api.Account'),
        ),
    ]
