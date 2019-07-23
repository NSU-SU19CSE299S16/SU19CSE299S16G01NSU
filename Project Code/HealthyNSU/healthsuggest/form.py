from django import forms
from .models import *

class CommentForm(form.ModelForm)
	class Meta:
		model = Comment 
		fields = ('Name','Email','Body')
