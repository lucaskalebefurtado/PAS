# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Aluno (models.Model):
	nome = models.CharField(max_length=128)
	matricula = models.CharField(max_length=128)
	email = models.EmailField()
	

	def __str__(self):
		return self.nome

