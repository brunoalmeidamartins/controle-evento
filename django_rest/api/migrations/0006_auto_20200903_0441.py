# Generated by Django 3.1 on 2020-09-03 04:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20200903_0435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento_funcionario',
            name='convidado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.convidado'),
        ),
    ]
