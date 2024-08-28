from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def wszystkie_filmy(request):
    # return HttpResponse("<h1>To jest nasz pierwszy test</h1>")
    return render(request, 'filmy.html')