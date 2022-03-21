from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import *
from .models import *


def index(request):
	genres = Genre.objects.all()
	films = Film.objects.all()
	data = {
		"films": films,
		'items': genres,
		'is_cat_selected': 0
	}
	return render(request, 'films_gallery/index.html', context=data)


def show_genre(request, genre_slug):
	films = Film.objects.filter(genre=Genre.objects.get(slug=genre_slug))
	data = {
		"films": films,
		'is_cat_selected': 1
	}
	return render(request, 'films_gallery/index.html', context=data)


def info_about_film(request, film_slug):
	film = Film.objects.get(slug=film_slug)
	data = {
		"film": film
	}
	return render(request, 'films_gallery/info_about.html', context=data)


def add_film(request):
	if request.method == 'POST':
		form = AddFilmForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('home')

	else:
		form = AddFilmForm()
	data = {
		'form': form,
		'is_cat_selected': 1,
	}
	return render(request, "films_gallery/addpage.html", context=data)
