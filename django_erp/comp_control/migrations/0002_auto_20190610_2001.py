# Generated by Django 2.2.1 on 2019-06-10 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comp_control', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='component',
            name='minus',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='component',
            name='plus',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='component',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='trashcomponents',
            name='count_group_detail',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]