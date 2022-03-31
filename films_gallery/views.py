from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView

from .forms import *
from .models import *


class SearchFilm(ListView):
	model = Film
	template_name = 'films_gallery/index.html'
	context_object_name = 'films'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		context['is_cat_selected'] = 1
		context['title'] = 'Поиск'
		return context

	def get_queryset(self):
		if self.request.GET.get('search'):
			search_word = self.request.GET.get('search')
			films_objects = Film.objects.filter(title__icontains=search_word)
			return films_objects
		else:
			return Film.objects.all()


class FilmHome(ListView):
	paginate_by = 9
	model = Film
	template_name = 'films_gallery/index.html'
	context_object_name = 'films'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		context['items'] = Genre.objects.all()
		context['is_cat_selected'] = 0
		context['title'] = 'Фильмы'
		return context


class FilmGenre(ListView):
	paginate_by = 9
	model = Film
	template_name = 'films_gallery/index.html'
	context_object_name = 'films'

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


class ShowProducer(DetailView):
	model = Producer
	template_name = 'films_gallery/info_producer.html'
	slug_url_kwarg = 'producer_slug'
	context_object_name = "producer"


class RegisterUser(CreateView):
	form_class = RegisterForm
	template_name = 'films_gallery/register.html'

	def form_valid(self, form):
		user = form.save()
		login(self.request, user)
		return redirect('home')


class LoginUser(LoginView):
	form_class = AuthenticationForm
	template_name = 'films_gallery/login.html'


def logout_user(request):
	logout(request)
	return redirect('login')


def addcomment(request, film_slug, user_id):
	if request.POST['text'] != '':
		film = Film.objects.get(slug=film_slug)
		comment = Comment.objects.create(content=request.POST['text'], user=User.objects.get(pk=user_id))
		film.comment.add(comment)
	return redirect("info-about", film_slug=film_slug)
