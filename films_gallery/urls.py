from django.urls import path
from .views import *

urlpatterns = [
	path('', FilmHome.as_view(), name='home'),
	path('<slug:genre_slug>/', FilmGenre.as_view(), name='show-genre'),
	path('about/<slug:film_slug>', ShowFilm.as_view(), name='info-about'),
	path('add', AddFilm.as_view(), name='add-film'),
	path('register', RegisterUser.as_view(), name="register"),
	path('login', LoginUser.as_view(), name="login"),
	path('logout', logout_user, name="logout"),
	path('producer/<slug:producer_slug>', ShowProducer.as_view(), name='info-producer'),
	path('addcomment/<slug:film_slug>/<int:user_id>', addcomment, name='addcomment')
]
