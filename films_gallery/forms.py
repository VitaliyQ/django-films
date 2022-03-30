from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *


class AddFilmForm(forms.ModelForm):
	class Meta:
		model = Film
		fields = ('title', 'en_title', 'slang', 'slug', 'content', 'date_publisher', 'time', 'rating', 'genre', 'photo',
		          'producer')
		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Название фильмы'}),
			'en_title': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Название на английской'}),
			'content': forms.TextInput(attrs={'class': 'content-input', 'placeholder': 'Описание фильма'}),
			'slang': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Краткое описание'}),
			'slug': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Адрес'}),
			'date_publisher': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'ГГГГ-ММ-ДД'}),
			'genre': forms.SelectMultiple(attrs={'class': 'genre-choose'})
		}


class RegisterForm(UserCreationForm):
	username = forms.CharField(label="Логин",
	                           widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Имя пользователя'}))
	email = forms.EmailField(label="Email",
	                         widget=forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'E-mail адрес'}))
	password1 = forms.CharField(label="Пароль",
	                            widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Пароль'}))
	password2 = forms.CharField(label="Повтор пароля",
	                            widget=forms.PasswordInput(
		                            attrs={'class': 'form-input', 'placeholder': 'Подтверждение пароля'}))

	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')
