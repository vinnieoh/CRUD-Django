# Generated by Django 2.2.24 on 2021-10-11 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produto',
            old_name='nome',
            new_name='produto',
        ),
    ]
