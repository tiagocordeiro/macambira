from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class Beer(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, verbose_name="Slug / URL",
                            help_text="Preenchido automaticamente, não editar.",
                            null=True,
                            blank=True, )
    description = models.TextField()
    image = models.ImageField(
        verbose_name="Imagem",
        upload_to='cervejas/',
        null=True,
        blank=True,
    )
    abv = models.DecimalField(
        verbose_name="Alcohol By Volume",
        decimal_places=2,
        max_digits=4,
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
    created_date = models.DateTimeField(default=timezone.now)
    added_by = models.ForeignKey(User,
                                 blank=True, null=True,
                                 on_delete=models.SET_NULL
                                 )
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name', 'category', 'style')
        verbose_name = 'cerveja'
        verbose_name_plural = 'cervejas'

    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def save(self):
        self.slug = slugify(self.name)
        super(Beer, self).save()

    def __str__(self):
        return self.name


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
