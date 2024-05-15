# Generated by Django 5.0.4 on 2024-05-13 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UsuarioRegistrado',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('contraseña', models.CharField(max_length=100)),
                ('dni', models.CharField(max_length=10, unique=True)),
                ('fecha_nacimiento', models.DateField()),
            ],
        ),
    ]
