# Generated by Django 2.2.1 on 2019-06-10 22:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comp_control', '0007_auto_20190610_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component',
            name='analog',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='comp_control.Component'),
        ),
        migrations.AlterField(
            model_name='component',
            name='name',
            field=models.CharField(default=1, max_length=100, verbose_name='Name'),
            preserve_default=False,
        ),
    ]