"""
URL configuration for filmy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from rest_framework import routers
from projekt_filmy.filmyweb.views import UserView, FilmView


router = routers.DefaultRouter()
router.register(r'users', UserView)
router.register(r'filmy', FilmView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('filmy/', include('projekt_filmy.filmyweb.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    # wersja na prod -> https://docs.djangoproject.com/en/5.1/howto/static-files/deployment/
    path('', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # wersja na development -> https://docs.djangoproject.com/en/5.1/howto/static-files/#serving-files-uploaded-by-a-user-during-development