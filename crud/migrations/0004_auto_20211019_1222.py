# Generated by Django 2.2.24 on 2021-10-19 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0003_auto_20211019_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='preco',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='produto',
            name='quantidade',
            field=models.IntegerField(default=0),
        ),
    ]
