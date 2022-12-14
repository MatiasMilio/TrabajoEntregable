# Generated by Django 4.1.2 on 2022-11-02 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_configuracion_titulo_principal'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuracion',
            name='subtitulo_principal',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='configuracion',
            name='construido_por',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='configuracion',
            name='nombre_blog',
            field=models.CharField(default='', max_length=14),
        ),
        migrations.AlterField(
            model_name='configuracion',
            name='titulo_principal',
            field=models.CharField(default='', max_length=30),
        ),
    ]
