# Generated by Django 3.1.2 on 2020-10-19 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20201019_0051'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='slug',
            field=models.SlugField(max_length=200, null=True, unique=True),
        ),
    ]