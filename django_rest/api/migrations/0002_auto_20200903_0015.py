# Generated by Django 3.1 on 2020-09-03 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='total_arrecado',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='evento',
            name='total_gasto',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='evento',
            name='total_gasto_bebida',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='evento',
            name='total_gasto_comida',
            field=models.FloatField(blank=True),
        ),
    ]
