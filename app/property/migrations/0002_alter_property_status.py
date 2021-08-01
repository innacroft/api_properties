# Generated by Django 3.2.5 on 2021-08-01 01:14

from django.db import migrations, models
import property.constants


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='status',
            field=models.IntegerField(choices=[(property.constants.PropertyStatus['PRE_SOLD'], 1), (
                property.constants.PropertyStatus['AVAILABLE'], 2), (property.constants.PropertyStatus['SOLD'], 3)], default=0),
        ),
    ]
