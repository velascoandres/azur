# Generated by Django 2.2.1 on 2019-06-14 06:39

import apps.inmuebles.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to=apps.inmuebles.models.user_directory_path)),
            ],
        ),
        migrations.CreateModel(
            name='TipoInmueble',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_tipo', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Inmueble',
            fields=[
                ('predio', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('ubicacion', models.CharField(max_length=50)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('titulo', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=180)),
                ('activo', models.BooleanField(default=True)),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inmuebles.TipoInmueble')),
            ],
        ),
    ]