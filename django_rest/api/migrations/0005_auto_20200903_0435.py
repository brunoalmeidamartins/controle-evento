# Generated by Django 3.1 on 2020-09-03 04:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200903_0332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento_funcionario',
            name='convidado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.convidado'),
        ),
    ]
