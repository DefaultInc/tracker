# Generated by Django 2.0 on 2017-12-08 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20171208_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='price',
            field=models.DecimalField(decimal_places=4, max_digits=10),
        ),
    ]