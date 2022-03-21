from django import forms
from .models import *


class AddFilmForm(forms.ModelForm):
	class Meta:
		model = Film
		fields = ['title', 'en_title', 'slang', 'slug', 'content', 'date_publisher', 'time', 'rating', 'genre', 'photo']
		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Название фильмы'}),
			'en_title': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Название на английской'}),
			'content': forms.TextInput(attrs={'class': 'content-input', 'placeholder': 'Описание фильма'}),
			'slang': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Краткое описание'}),
			'slug': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Адрес'}),
			'date_publisher': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'ГГГГ-ММ-ДД'}),
			'genre': forms.SelectMultiple(attrs={'class': 'genre-choose'})

		}
