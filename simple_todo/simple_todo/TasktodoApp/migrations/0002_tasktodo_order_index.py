# Generated by Django 4.2.7 on 2023-12-19 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TasktodoApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasktodo',
            name='order_index',
            field=models.IntegerField(default=0),
        ),
    ]
