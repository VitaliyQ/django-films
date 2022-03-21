from django.urls import path, include
from .views import *

urlpatterns = [
	path('', index, name='home'),
	path('<slug:genre_slug>/', show_genre, name='show-genre'),
	path('about/<slug:film_slug>', info_about_film, name='info-about'),
	path('add', add_film, name='add-film')
]
