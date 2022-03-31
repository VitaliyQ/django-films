from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Genre(models.Model):
	name = models.CharField(max_length=30, unique=True, verbose_name="Название")
	slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

	def get_absolute_url(self):
		return reverse('show-genre', kwargs={"genre_slug": self.slug})

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Жанры'
		verbose_name_plural = 'Жанры'
		ordering = ['name']


class Producer(models.Model):
	name = models.CharField(max_length=30, blank=False, unique=True, verbose_name="Имя")
	slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
	genre = models.ManyToManyField('Genre', blank=False, verbose_name="Жанры")
	place_of_birth = models.CharField(max_length=30, blank=True, null=True, verbose_name="Место рождения")
	date_of_birth = models.DateField(blank=True, verbose_name="Дата рождения", null=True)
	photo = models.ImageField(blank=True, upload_to="photos/%Y/%m/%d/", null=True, verbose_name='Фото')

	def get_absolute_url(self):
		return reverse('info-producer', kwargs={"producer_slug": self.slug})

	def __str__(self):
		return f"{self.name}"

	def __repr__(self):
		return self.name

	class Meta:
		verbose_name = 'Режиссеры'
		verbose_name_plural = 'Режиссеры'
		ordering = ['name']


class Film(models.Model):
	title = models.CharField(max_length=50, blank=True, unique=True, verbose_name='Название фильма')
	en_title = models.CharField(blank=True, max_length=50, null=True, verbose_name="Название на английском")
	slang = models.CharField(blank=True, max_length=255, null=True, default=None, verbose_name='Краткое описание')
	slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
	content = models.TextField(verbose_name='Описание фильма')
	photo = models.ImageField(blank=True, upload_to="photos/%Y/%m/%d/", null=True, verbose_name='Фото')
	date_publisher = models.DateField(verbose_name='Дата выхода фильма')
	time = models.IntegerField(blank=True, verbose_name='Длительность фильма')
	rating = models.IntegerField(default=0, verbose_name='Рейтинг фильма (0, 100)')
	genre = models.ManyToManyField('Genre', verbose_name='Жанр')
	producer = models.ManyToManyField('Producer', blank=False, verbose_name='Режиссер')
	comment = models.ManyToManyField('Comment', null=True)

	def get_absolute_url(self):
		return reverse('info-about', kwargs={"film_slug": self.slug})

	def __str__(self):
		return f"{self.id}. {self.title}, дата премьеры - {self.date_publisher}, рейтинг - {self.rating}"

	def __repr__(self):
		return self.title

	class Meta:
		verbose_name = 'Фильмы'
		verbose_name_plural = 'Фильмы'
		ordering = ['title']


class Comment(models.Model):
	content = models.TextField(verbose_name='Комментарий', max_length=500)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f"{self.id}. {self.content}"

	def __repr__(self):
		return self.content

	class Meta:
		verbose_name = 'Коментарии'
		verbose_name_plural = 'Коментарии'
		ordering = ['film']
