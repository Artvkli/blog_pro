# Generated by Django 4.2.11 on 2024-03-26 20:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_article_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2024, 3, 26, 20, 24, 42, 101454, tzinfo=datetime.timezone.utc)),
        ),
    ]
