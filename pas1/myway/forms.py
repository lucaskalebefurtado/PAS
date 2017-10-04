from django.forms import ModelForm
from myway.models import Aluno
	

class AlunoForm(ModelForm):
	class Meta:
		model = Aluno
		fields = ["nome", "matricula", "email"]


