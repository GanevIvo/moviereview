# Generated by Django 3.2.12 on 2022-04-26 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_movie_movie_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='movie_cover',
            field=models.ImageField(upload_to='movie_covers/'),
        ),
    ]
