# Generated by Django 3.2.7 on 2021-09-30 23:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_auto_20210928_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='curso_publicado',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 30, 18, 34, 19, 728908), verbose_name='fecha de publicacion'),
        ),
        migrations.AlterField(
            model_name='registrom',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 30, 18, 34, 19, 729907), verbose_name='fecha de matricula'),
        ),
    ]
