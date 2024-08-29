from django.urls import path
from projekt_filmy.filmyweb.views import wszystkie_filmy, nowy_film, edytuj_film, usun_film


urlpatterns = [
    path('wszystkie/', wszystkie_filmy, name='wszystkie'),
    path('nowy/', nowy_film, name='nowy_film'),
    path('edytuj/<int:id>/', edytuj_film, name='edit_film'),
    path('usun/<int:id>/', usun_film, name='usun_film'),
]