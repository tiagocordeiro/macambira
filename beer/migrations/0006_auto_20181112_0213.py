# Generated by Django 2.1.2 on 2018-11-12 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beer', '0005_auto_20181015_0318'),
    ]

    operations = [
        migrations.AddField(
            model_name='beer',
            name='examples',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Exemplos'),
        ),
        migrations.AlterField(
            model_name='beer',
            name='abv',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Alcohol By Volume'),
        ),
        migrations.AlterField(
            model_name='beer',
            name='ibu',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='International Bitterness Units'),
        ),
        migrations.AlterField(
            model_name='beer',
            name='srm',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Standard Reference Method'),
        ),
    ]
