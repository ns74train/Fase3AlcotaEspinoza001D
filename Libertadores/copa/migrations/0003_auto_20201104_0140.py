# Generated by Django 3.1.2 on 2020-11-04 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('copa', '0002_auto_20201103_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='rut',
            field=models.CharField(help_text='ingrese 8 Caracteres', max_length=8, primary_key=True, serialize=False),
        ),
    ]
