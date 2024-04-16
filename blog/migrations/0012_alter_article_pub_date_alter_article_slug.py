# Generated by Django 4.2.11 on 2024-04-07 20:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_article_pub_date_alter_article_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2024, 4, 7, 20, 10, 56, 376700, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
