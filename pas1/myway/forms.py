from django import forms
from .models import Cliente


class AlunoForm(forms.Form):
	username = forms.CharField(label='username',)
	password = forms.CharField(label='Senha')
class LoginForm(forms.Form):
	username = forms.CharField(label='username',)
	password = forms.CharField(label='Senha')


