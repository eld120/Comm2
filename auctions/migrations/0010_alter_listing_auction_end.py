# Generated by Django 3.2.12 on 2022-03-16 20:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_auto_20220315_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='auction_end',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 23, 20, 2, 4, 367769, tzinfo=utc), null=True),
        ),
    ]
