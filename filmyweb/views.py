from django.shortcuts import render
from django.http import HttpResponse

from .forms import FilmForm
from .models import Film

# Create your views here.

def wszystkie_filmy(request):
    # return HttpResponse("<h1>To jest nasz pierwszy test</h1>")
    # test = ["avatar", "titanic"]

    # read>
    wszystkie = Film.objects.all()
    # wszystkie = Film.objects.get(id=1)
    # wszystkie = Film.objects.filter(id=1)
    # <read

    # jeden = Film.objects.get(tytul='Titanic')
    # jeden = Film.objects.filter(tytul='Titanic')

    # Film.objects.create(tytul='Jakis1', rok=2020, opis='jakis5')

    # film = Film.objects.get(id=5)
    # film.tytul = 'Terminal'
    # film.save()

    # film.delete()
    # lub
    # Film.objects.get(id=5).delete()

    # dla get trzeba dac nawiassy []
    # return render(request, 'filmy.html', {'filmy': [wszystkie]})
    return render(request, 'filmy.html', {'filmy': wszystkie})

def nowy_film(request):
    form = FilmForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()

    return render(request, 'nowy_film.html', {'form': form})