# Generated by Django 3.0.7 on 2020-06-22 21:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Todos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
