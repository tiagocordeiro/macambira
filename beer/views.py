from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import BeerForm
from .models import Beer


@login_required
def beer_create(request):
    if request.method == 'POST':
        form = BeerForm(request.POST)
        if form.is_valid():
            beer = form.save(commit=False)
            beer.added_by = request.user
            beer.save()
            return redirect(beer_list)

    else:
        form = BeerForm()

    return render(request, 'beer/beer_create.html', {'form': form})


def beer_list(request):
    beers = Beer.objects.all()
    context = {'beers': beers}
    return render(request, 'beer/beer_list.html', context)


def beer_details(request, slug):
    beer = get_object_or_404(Beer, slug=slug)
    return render(request, 'beer/beer_details.html', {'beer': beer})
