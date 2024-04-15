# Generated by Django 5.0.3 on 2024-04-04 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_contatomodel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contatomodel',
            options={'ordering': ['-created_at'], 'verbose_name': 'Forlumário de Contato'},
        ),
        migrations.AlterModelOptions(
            name='examplemodel',
            options={'ordering': ['name'], 'verbose_name': 'Formulário de Exemplo'},
        ),
        migrations.AddField(
            model_name='contatomodel',
            name='read',
            field=models.BooleanField(blank=True, default=False, verbose_name='Lido'),
        ),
    ]