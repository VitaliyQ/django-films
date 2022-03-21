from django.urls import path, include
from .views import *

urlpatterns = [
	path('', FilmHome.as_view(), name='home'),
	path('<slug:genre_slug>/', FilmCategory.as_view(), name='show-genre'),
	path('about/<slug:film_slug>', ShowFilm.as_view(), name='info-about'),
	path('add', AddFilm.as_view(), name='add-film'),
	path('producer/<slug:producer_slug>', ShowProducer.as_view(), name='info-producer')
]
