from django.contrib import admin
from .models import *


class FilmAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'photo')
	list_display_links = ('id', 'title')
	search_fields = ('title', 'content')
	prepopulated_fields = {"slug": ("title",)}


class GenreAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')
	list_display_links = ('id', 'name')
	prepopulated_fields = {"slug": ("name",)}


admin.site.register(Film, FilmAdmin)
admin.site.register(Genre)
