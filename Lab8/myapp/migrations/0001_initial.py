# Generated by Django 5.1.1 on 2024-09-15 12:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cinema_name', models.CharField(max_length=255)),
                ('ticket_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('seat_count', models.PositiveIntegerField()),
                ('address', models.CharField(max_length=255)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=255)),
                ('genre', models.CharField(choices=[('Melodrama', 'Melodrama'), ('Comedy', 'Comedy'), ('Action', 'Action')], max_length=50)),
                ('duration', models.PositiveIntegerField()),
                ('rating', models.DecimalField(decimal_places=1, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='MovieScreening',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('screening_days', models.PositiveIntegerField()),
                ('cinema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.cinema')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.movie')),
            ],
        ),
    ]
