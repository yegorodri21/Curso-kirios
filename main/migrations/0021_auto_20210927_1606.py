# Generated by Django 3.2.7 on 2021-09-27 21:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20210927_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='curso_publicado',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 27, 16, 6, 56, 521702), verbose_name='fecha de publicacion'),
        ),
        migrations.AlterField(
            model_name='matriculados',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 27, 16, 6, 56, 523702), verbose_name='fecha de matricula'),
        ),
        migrations.AlterField(
            model_name='registrom',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 27, 16, 6, 56, 522703), verbose_name='fecha de matricula'),
        ),
    ]
