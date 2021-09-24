# Generated by Django 3.2.7 on 2021-09-23 21:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_curso_curso_publicado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='curso_publicado',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 23, 16, 20, 56, 433780), verbose_name='fecha de publicacion'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='foto',
            field=models.ImageField(null=True, upload_to='albums', verbose_name='albums'),
        ),
    ]
