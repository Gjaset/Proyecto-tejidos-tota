# Generated by Django 4.0.4 on 2022-04-21 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_usuario_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='rol',
            field=models.CharField(choices=[('Administrador', 'Administrador'), ('Proveedor', 'Proveedor'), ('Asociada', 'Asociada'), ('Cliente', 'Cliente')], max_length=13, verbose_name='rol'),
        ),
    ]