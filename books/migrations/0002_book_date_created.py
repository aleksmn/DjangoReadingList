# Generated by Django 2.1 on 2020-08-11 09:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
