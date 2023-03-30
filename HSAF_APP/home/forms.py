from django import forms
from home.models import Posts

class newtripform(forms.ModelForm):
	class Meta:
			model = Posts
			fields = ['title', 'content']