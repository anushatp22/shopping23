# Generated by Django 3.2.8 on 2022-12-29 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='register_tb',
            name='status',
            field=models.CharField(default='pending', max_length=20),
        ),
    ]
