# Generated by Django 4.1.7 on 2023-04-02 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppProyectoFinalGavino', '0005_newsletter_alter_contacto_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='celular',
            field=models.IntegerField(),
        ),
    ]
