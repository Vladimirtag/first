# Generated by Django 2.2.1 on 2019-06-05 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comp_control', '0018_auto_20190605_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trashcomponents',
            name='count_group_detail',
            field=models.IntegerField(blank=True, verbose_name='количество плат'),
        ),
        migrations.AlterField(
            model_name='trashcomponents',
            name='write_off_ditail_in_bom',
            field=models.ManyToManyField(blank=True, to='comp_control.QuantityComponent'),
        ),
    ]