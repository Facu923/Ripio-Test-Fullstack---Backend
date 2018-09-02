# Generated by Django 2.1 on 2018-08-31 23:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_remove_client_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='accounts', to='api.Client'),
        ),
        migrations.AlterField(
            model_name='account',
            name='id',
            field=models.AutoField(db_column='id', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='account',
            name='number',
            field=models.BigIntegerField(auto_created=True),
        ),
    ]
