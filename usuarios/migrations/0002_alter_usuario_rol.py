# Generated by Django 4.0.3 on 2022-04-19 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='rol',
            field=models.CharField(choices=[('A', 'Administrador'), ('P', 'Proveedor'), ('As', 'Asociada'), ('C', 'Cliente')], max_length=2, verbose_name='rol'),
        ),
    ]
