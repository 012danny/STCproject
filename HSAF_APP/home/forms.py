from django import forms
from django.forms import ModelForm
from home.models import posts
from home.models import AuthUser


class newtripform(forms.ModelForm):   # form / informaiton we will ask user for. 
	class Meta:         
			model = posts
			fields = ['title', 'content']

	