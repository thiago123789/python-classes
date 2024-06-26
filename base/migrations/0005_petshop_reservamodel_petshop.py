# Generated by Django 5.0.3 on 2024-05-06 22:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_reservamodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Petshop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('rua', models.CharField(max_length=100, verbose_name='Rua')),
                ('numero', models.CharField(max_length=100, verbose_name='Número')),
                ('bairro', models.CharField(max_length=50, verbose_name='Bairro')),
            ],
        ),
        migrations.AddField(
            model_name='reservamodel',
            name='petshop',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reservas', to='base.petshop'),
        ),
    ]
