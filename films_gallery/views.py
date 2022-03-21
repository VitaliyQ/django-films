from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView

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
	allow_empty = False

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		context['is_cat_selected'] = 1
		context['title'] = Genre.objects.get(slug=self.kwargs['genre_slug']).name
		return context

	def get_queryset(self):
		return Film.objects.filter(genre__slug=self.kwargs['genre_slug'])


class ShowFilm(DetailView):
	model = Film
	template_name = 'films_gallery/info_about.html'
	slug_url_kwarg = 'film_slug'
	context_object_name = "film"


class AddFilm(CreateView):
	form_class = AddFilmForm
	template_name = 'films_gallery/addpage.html'
