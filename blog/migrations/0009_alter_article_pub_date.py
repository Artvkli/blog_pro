# Generated by Django 4.2.11 on 2024-04-07 19:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_article_slug_alter_article_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2024, 4, 7, 19, 59, 58, 454050, tzinfo=datetime.timezone.utc)),
        ),
    ]
