# Generated by Django 3.2.12 on 2022-04-26 17:50

from django.db import migrations, models
import movie_review_project.common.validators


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviereviewuser',
            name='username',
            field=models.CharField(max_length=25, unique=True, validators=[movie_review_project.common.validators.validate_only_alphanumeric]),
        ),
    ]
