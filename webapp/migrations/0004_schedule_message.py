# Generated by Django 4.2.6 on 2024-01-21 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_schedule_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='message',
            field=models.CharField(max_length=255, null=True),
        ),
    ]