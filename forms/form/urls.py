from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('menu/',views.menu),
    path('opisanie/',views.opisanie),
   # path('price/',views.price),
]