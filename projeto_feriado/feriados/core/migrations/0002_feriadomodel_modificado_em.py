# Generated by Django 5.0.3 on 2024-04-12 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feriadomodel',
            name='modificado_em',
            field=models.DateTimeField(auto_now=True, verbose_name='Modificado em'),
        ),
    ]
