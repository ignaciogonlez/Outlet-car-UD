# Generated by Django 5.1.3 on 2024-12-01 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appOutletDjango', '0002_remove_coche_categorias_coche_categoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coche',
            name='categoria',
        ),
        migrations.AddField(
            model_name='coche',
            name='categorias',
            field=models.ManyToManyField(related_name='coches', to='appOutletDjango.categoria'),
        ),
    ]
