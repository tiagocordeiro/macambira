from django.shortcuts import render


def index(request):
    data = {'mydebug': True}
    return render(request, 'index.html', data)
