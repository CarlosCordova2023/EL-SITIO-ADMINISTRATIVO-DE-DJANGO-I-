# Generated by Django 4.0.5 on 2024-09-29 00:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0004_alter_book_fecha_creacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='fecha_creacion',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='libro',
            name='fecha_modificacion',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]
