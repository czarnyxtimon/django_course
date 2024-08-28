from django.shortcuts import render
from django.http import HttpResponse
from .models import Film

# Create your views here.

def wszystkie_filmy(request):
    # return HttpResponse("<h1>To jest nasz pierwszy test</h1>")
    # test = ["avatar", "titanic"]
    wszystkie = Film.objects.all()
    # jeden = Film.objects.get(tytul='Titanic')
    # jeden = Film.objects.filter(tytul='Titanic')

    # Film.objects.create(tytul='Jakis1', rok=2020, opis='jakis5')

    # film = Film.objects.get(id=5)
    # film.tytul = 'Terminal'
    # film.save()

    # film.delete()
    # lub
    # Film.objects.get(id=5).delete()

    return render(request, 'filmy.html', {'filmy': wszystkie})

