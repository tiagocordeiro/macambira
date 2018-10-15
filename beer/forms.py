from django.forms import ModelForm

from .models import Beer


class BeerForm(ModelForm):
    class Meta:
        model = Beer
        fields = ['name', 'description', 'image', 'abv', 'ibu', 'srm', 'style', 'category', ]
