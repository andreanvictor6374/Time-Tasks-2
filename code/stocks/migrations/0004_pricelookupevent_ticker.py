# Generated by Django 3.1.2 on 2020-11-05 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0003_auto_20201104_2359'),
    ]

    operations = [
        migrations.AddField(
            model_name='pricelookupevent',
            name='ticker',
            field=models.CharField(default='appl', max_length=20),
            preserve_default=False,
        ),
    ]