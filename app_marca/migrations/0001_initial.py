# Generated by Django 5.2.4 on 2025-07-16 00:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True, verbose_name='Marca')),
            ],
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Modelo')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modelos', to='app_marca.marca')),
            ],
            options={
                'unique_together': {('marca', 'nome')},
            },
        ),
    ]
