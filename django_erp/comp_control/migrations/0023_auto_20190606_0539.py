# Generated by Django 2.2.1 on 2019-06-06 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comp_control', '0022_auto_20190606_0432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trashcomponents',
            name='count_group_detail',
            field=models.IntegerField(blank=True, null=True, verbose_name='количество плат'),
        ),
    ]