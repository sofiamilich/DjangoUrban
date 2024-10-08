# Generated by Django 5.0.7 on 2024-08-12 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('balance', models.DecimalField(decimal_places=10, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=500)),
                ('cost', models.DecimalField(decimal_places=10, max_digits=10)),
                ('size', models.DecimalField(decimal_places=10, max_digits=10)),
                ('description', models.TextField(max_length=500)),
                ('age_limited', models.BooleanField(default=False)),
                ('field_fractional_numbers', models.DecimalField(decimal_places=10, max_digits=10)),
                ('buyer', models.ManyToManyField(related_name='games', to='task1.buyer')),
            ],
        ),
    ]
