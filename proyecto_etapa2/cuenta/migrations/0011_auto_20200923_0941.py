# Generated by Django 3.1.1 on 2020-09-23 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuenta', '0010_auto_20200923_0804'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comentario',
            old_name='com_trabajor',
            new_name='com_trabajador',
        ),
        migrations.AlterField(
            model_name='recomendaciones',
            name='recomendaciones',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
