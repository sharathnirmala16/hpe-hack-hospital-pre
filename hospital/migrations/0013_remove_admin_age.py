# Generated by Django 3.1.5 on 2021-05-02 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0012_auto_20210502_1140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin',
            name='age',
        ),
    ]
