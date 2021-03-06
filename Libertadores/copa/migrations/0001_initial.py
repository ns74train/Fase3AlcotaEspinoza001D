# Generated by Django 3.1.2 on 2020-10-19 14:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('rut', models.UUIDField(default=uuid.uuid4, help_text='Unico dato de personas', primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('correo', models.CharField(max_length=100)),
                ('contraseña', models.CharField(max_length=100)),
                ('recontraseña', models.CharField(max_length=100)),
                ('Direccion', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
    ]
