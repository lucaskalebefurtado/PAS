# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Aluno (models.Model):
	nome = models.CharField(max_length=50)
	username = models.CharField(max_length=50, default = "user")
	email = models.EmailField()
	matricula = models.CharField(max_length=50)
	senha = models.CharField(max_length=50)
	
	
	sexo_choices = (("Masculino", "Masculino"),("Feminino", "Feminino"),("Não-declarado", "Não-declarado"),)
	sexo = models.CharField(
        max_length=20,
        choices=sexo_choices,
        )
        
        
        
	periodo_choices = (("2008.1", "08.1"),("2009.1", "09.1"),
	("2010.1", "10.1"), ("2011.1", "11.1"),("2012.1", "12.1"),("2013.1", "13.1"),("2014.1", "14.1"),
	("2015.1", "15.1"),	("2016.1", "16.1")) #lembrar de atualizar todo período que se inicia
	periodo = models.CharField( max_length=20,choices=periodo_choices,)
    
    
    
	def __str__(self):
		return self.nome

