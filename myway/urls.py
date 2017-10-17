from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^login', views.user_login, name='login'),
	url(r'^cadastro', views.cadastro, name='cadastro'), 
	url (r'^fluxograma', views.fluxograma, name='fluxograma'),	
	url(r'^restrita', views.restricted_area,name='restrited_area'),
	url(r'^telauser', views.telauser,name='telauser'),
	url(r'^perfil', views.perfil, name= 'perfil')]