# Generated by Django 3.2.12 on 2022-03-04 03:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_auto_20220302_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='auction_end',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 11, 3, 43, 43, 33109, tzinfo=utc), null=True),
        ),
    ]
