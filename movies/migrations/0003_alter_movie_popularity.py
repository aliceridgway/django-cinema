# Generated by Django 4.0.5 on 2022-06-02 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_alter_movie_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='popularity',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
