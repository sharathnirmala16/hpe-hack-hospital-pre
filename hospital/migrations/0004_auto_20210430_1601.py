# Generated by Django 3.1.5 on 2021-04-30 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0003_charges_medicines'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charges',
            name='unitprice',
            field=models.FloatField(default=0),
        ),
    ]
