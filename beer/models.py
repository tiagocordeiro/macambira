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
    abv = models.CharField(
        verbose_name="Alcohol By Volume",
        max_length=10,
        null=True,
        blank=True,
    )
    ibu = models.CharField(
        verbose_name="International Bitterness Units",
        max_length=10,
        null=True,
        blank=True,
    )
    srm = models.CharField(
        verbose_name="Standard Reference Method",
        max_length=10,
        null=True,
        blank=True,
    )
    examples = models.CharField(
        verbose_name="Exemplos",
        max_length=200,
        null=True,
        blank=True,

    )
    original_gravity = models.CharField(
        verbose_name='Gravidade Inicial',
        max_length=20,
        blank=True,
        null=True
    )
    final_gravity = models.CharField(
        verbose_name='Gravidade Final',
        max_length=20,
        blank=True,
        null=True
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    style = models.ForeignKey(
        'Style',
        on_delete=models.SET_NULL,
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

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)

        super(Beer, self).save(*args, **kwargs)

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
