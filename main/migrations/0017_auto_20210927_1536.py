# Generated by Django 3.2.7 on 2021-09-27 20:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20210927_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='curso_publicado',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 27, 15, 36, 51, 893061), verbose_name='fecha de publicacion'),
        ),
        migrations.AlterField(
            model_name='matriculados',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 27, 15, 36, 51, 896062), verbose_name='fecha de matricula'),
        ),
        migrations.AlterField(
            model_name='registrom',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 27, 15, 36, 51, 895063), verbose_name='fecha de matricula'),
        ),
    ]
