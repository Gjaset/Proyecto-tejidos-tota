# Generated by Django 4.0.3 on 2022-04-19 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=50, verbose_name='Apellido')),
                ('documento', models.CharField(max_length=10, unique=True)),
                ('celular', models.CharField(max_length=10, unique=True)),
                ('tipo_documento', models.CharField(choices=[('C.C', 'C.C'), ('T.I', 'T.I'), ('C.E', 'C.E')], max_length=3, verbose_name='Tipo_documento')),
                ('rol', models.CharField(choices=[('A', 'Administrador'), ('P', 'Proveedor'), ('As', 'Asociada'), ('C', 'Cliente')], max_length=2, verbose_name='Rol')),
            ],
        ),
    ]