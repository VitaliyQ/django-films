from django import forms
from .models import *


class AddFilmForm(forms.ModelForm):
	class Meta:
		model = Film
		fields = '__all__'
