# Generated by Django 2.2 on 2019-05-04 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comp_control', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='serial_number',
            field=models.IntegerField(blank=True, verbose_name='serial_number'),
        ),
    ]
