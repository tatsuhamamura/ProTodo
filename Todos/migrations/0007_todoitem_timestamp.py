# Generated by Django 3.0.7 on 2020-06-23 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todos', '0006_auto_20200624_0217'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
