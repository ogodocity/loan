# Generated by Django 3.2.9 on 2023-01-10 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_system', '0030_alter_lender_conditions'),
    ]

    operations = [
        migrations.AddField(
            model_name='applyloan',
            name='file_1',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='applyloan',
            name='file_2',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='applyloan',
            name='file_3',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=''),
        ),
    ]
