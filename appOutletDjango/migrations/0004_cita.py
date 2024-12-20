# Generated by Django 5.1.3 on 2024-12-09 09:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appOutletDjango', '0003_remove_coche_categoria_coche_categorias'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre del usuario que agenda la cita', max_length=100)),
                ('email', models.EmailField(help_text='Correo electrónico para confirmar la cita', max_length=254)),
                ('telefono', models.CharField(blank=True, help_text='Teléfono de contacto', max_length=15)),
                ('fecha_cita', models.DateField(help_text='Fecha de la cita')),
                ('hora_cita', models.TimeField(help_text='Hora de la cita')),
                ('mensaje', models.TextField(blank=True, help_text='Mensaje adicional del usuario', max_length=500)),
                ('oferta', models.ForeignKey(help_text='Oferta vinculada a la cita', on_delete=django.db.models.deletion.CASCADE, related_name='citas', to='appOutletDjango.ofertacoche')),
            ],
        ),
    ]
