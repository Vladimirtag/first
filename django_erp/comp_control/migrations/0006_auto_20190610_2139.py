# Generated by Django 2.2.1 on 2019-06-10 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comp_control', '0005_auto_20190610_2137'),
    ]

    operations = [
        migrations.AddField(
            model_name='component',
            name='number_action',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='component',
            name='number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]