from django.core.management.base import BaseCommand
from beer.models import Beer, Category, Style
from django.utils.text import slugify

from utils.beer_populate import create_beers


class Command(BaseCommand):
    help = '''Pupula banco com cervejas'''

    def handle(self, *args, **options):
        beers = create_beers()
        new_beers = []
        for beer in beers:
            name = beer['name']
            slug = slugify(beer['name'])
            category = beer['category']
            style = beer['style']
            description = beer['description']
            examples = beer['examples']
            abv = beer['abv']
            ibu = beer['ibu']
            srm = beer['srm']
            original_gravity = beer['original_gravity']
            final_gravity = beer['final_gravity']
            new_beer = Beer(
                name=name,
                slug=slug,
                category=Category.objects.get(name=category),
                style=Style.objects.get(name=style),
                description=description,
                examples=examples,
                abv=abv,
                ibu=ibu,
                srm=srm,
                original_gravity=original_gravity,
                final_gravity=final_gravity,
            )
            new_beers.append(new_beer)
        Beer.objects.bulk_create(new_beers)
