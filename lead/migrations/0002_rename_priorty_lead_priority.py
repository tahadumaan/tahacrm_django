# Generated by Django 3.2.8 on 2021-10-24 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lead',
            old_name='priorty',
            new_name='priority',
        ),
    ]
