# Generated by Django 3.2.9 on 2022-04-11 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_system', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='balance',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12),
        ),
    ]
