# Generated by Django 2.1.2 on 2018-10-15 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beer', '0004_auto_20181015_0233'),
    ]

    operations = [
        migrations.AddField(
            model_name='beer',
            name='slug',
            field=models.SlugField(blank=True, help_text='Preenchido automaticamente, não editar.', max_length=255, null=True, unique=True, verbose_name='Slug / URL'),
        ),
        migrations.AlterField(
            model_name='beer',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
