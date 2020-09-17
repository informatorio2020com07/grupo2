# Generated by Django 3.1.1 on 2020-09-17 13:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bolsa', '0001_initial'),
        ('cuenta', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='oferta',
            name='categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cuenta.categoria'),
        ),
        migrations.AddField(
            model_name='oferta',
            name='oferente',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='oferta_creados', to=settings.AUTH_USER_MODEL),
        ),
    ]