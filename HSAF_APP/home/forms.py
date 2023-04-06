from django import forms
from django.forms import ModelForm
from home.models import posts
from home.models import AuthUser


class newtripform(forms.ModelForm):
	title = forms.TextInput()
	content = forms.TextInput()
	userid = forms.IntegerField()


	class Meta:
			model = posts
			fields = ['title', 'content', 'userid']