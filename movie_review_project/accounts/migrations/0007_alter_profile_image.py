# Generated by Django 3.2.12 on 2022-04-26 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_moviereviewuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='staticfiles/images/default-profile-picture.jpg', upload_to='profile_images/'),
        ),
    ]
