# Generated by Django 3.2.12 on 2022-04-25 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20220425_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='movie_star_actors',
            field=models.CharField(max_length=40),
        ),
    ]
