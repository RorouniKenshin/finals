# Generated by Django 4.2.6 on 2024-01-21 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='price',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='user',
        ),
    ]