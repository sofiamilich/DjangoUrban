# Generated by Django 5.0.7 on 2024-08-12 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='field_boolean_values',
            field=models.BooleanField(default=False),
        ),
    ]
