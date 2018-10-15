from django.db import models

from core.models import TimeStampedModel, Active


class Beer(models.Model, TimeStampedModel, Active):
    name = models.CharField(max_length=200)
    abv = models.PositiveIntegerField(
        verbose_name="Alcohol By Volume",
        null=True,
        blank=True,
    )
    ibu = models.PositiveIntegerField(
        verbose_name="International Bitterness Units",
        null=True,
        blank=True,
    )
    srm = models.PositiveIntegerField(
        verbose_name="Standard Reference Method",
        null=True,
        blank=True,
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    style = models.ForeignKey(
        'Style',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ('name', 'category', 'style')
        verbose_name = 'cerveja'
        verbose_name_plural = 'cervejas'


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ('name',)
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.name


class Style(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ('name',)
        verbose_name = 'estilo'
        verbose_name_plural = 'estilos'

    def __str__(self):
        return self.name
