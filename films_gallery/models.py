from django.db import models
from django.urls import reverse


class Genre(models.Model):
	name = models.CharField(max_length=30)
	slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

	def get_absolute_url(self):
		return reverse('show-genre', kwargs={"genre_slug": self.slug})

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Жанры'
		verbose_name_plural = 'Жанры'


class Film(models.Model):
	title = models.CharField(max_length=50, unique=True, verbose_name='Название фильма')
	en_title = models.CharField(max_length=50, null=True)
	slang = models.CharField(max_length=255, null=True, default=None)
	slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
	content = models.TextField()
	photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Фото')
	date_publisher = models.DateField()
	time = models.IntegerField()
	is_published = models.BooleanField()
	rating = models.IntegerField(default=0)
	genre = models.ManyToManyField('Genre')

	def get_absolute_url(self):
		return reverse('info-about', kwargs={"film_slug": self.slug})

	def __str__(self):
		return f"{self.title}, дата премьеры - {self.date_publisher}, рейтинг - {self.rating}"

	def __repr__(self):
		return self.title

	class Meta:
		verbose_name = 'Фильмы'
		verbose_name_plural = 'Фильмы'
		ordering = ['title']

# from films_gallery.models import Film
