# Generated by Django 2.0.4 on 2018-04-20 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock_ge',
            name='cahanges',
            field=models.IntegerField(),
        ),
    ]
