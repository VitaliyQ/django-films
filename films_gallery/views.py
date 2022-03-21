from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView

from .forms import *
from .models import *


class FilmHome(ListView):
	model = Film
	template_name = 'films_gallery/index.html'
	context_object_name = 'films'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		context['items'] = Genre.objects.all()
		context['is_cat_selected'] = 0
		context['title'] = 'Фильмы'
		return context


class FilmCategory(ListView):
	model = Film
	template_name = 'films_gallery/index.html'
	context_object_name = 'films'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		context['is_cat_selected'] = 1
		context['title'] = str(self.kwargs['genre_slug'])
		return context

	def get_queryset(self):
		return Film.objects.filter(genre__slug=self.kwargs['genre_slug'])


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
