# Generated by Django 3.2.7 on 2021-09-27 21:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20210927_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='curso_publicado',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 27, 16, 2, 20, 912793), verbose_name='fecha de publicacion'),
        ),
        migrations.AlterField(
            model_name='matriculados',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 27, 16, 2, 20, 914791), verbose_name='fecha de matricula'),
        ),
        migrations.AlterField(
            model_name='registrom',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 27, 16, 2, 20, 913792), verbose_name='fecha de matricula'),
        ),
    ]
