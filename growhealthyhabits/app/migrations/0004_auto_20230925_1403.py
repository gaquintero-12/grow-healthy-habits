# Generated by Django 3.1 on 2023-09-25 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20230921_1017'),
    ]

    operations = [
        migrations.AddField(
            model_name='presupuesto',
            name='egresos',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='presupuesto',
            name='ingresos',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
