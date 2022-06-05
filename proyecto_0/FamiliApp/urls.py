from django.urls import URLPattern
from FamiliApp.views import Familiares
from django.urls import path

urlpatterns = [
    path('', Familiares)
]