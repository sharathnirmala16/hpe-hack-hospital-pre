# Generated by Django 3.1.5 on 2021-05-02 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0014_admin_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin',
            name='status',
        ),
    ]
