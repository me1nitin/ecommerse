# Generated by Django 3.2.12 on 2022-03-09 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviesapp1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='ima',
            field=models.ImageField(blank=True, null=True, upload_to='gallery'),
        ),
    ]