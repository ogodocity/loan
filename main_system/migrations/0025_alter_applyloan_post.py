# Generated by Django 3.2.9 on 2023-01-05 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_system', '0024_alter_applyloan_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applyloan',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loans', to='main_system.lender'),
        ),
    ]
