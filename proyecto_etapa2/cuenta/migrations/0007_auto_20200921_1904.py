# Generated by Django 3.1.1 on 2020-09-21 22:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cuenta', '0006_auto_20200920_1844'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='titulo',
        ),
        migrations.AddField(
            model_name='perfil',
            name='categoria',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='perfil_de_categoria', to='cuenta.categoria'),
        ),
        migrations.AlterField(
            model_name='matricula_titulo',
            name='matricula',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
