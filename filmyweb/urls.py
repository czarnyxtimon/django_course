from django.urls import path
from filmyweb.views import test_response


urlpatterns = [
    path('test/', test_response)
]