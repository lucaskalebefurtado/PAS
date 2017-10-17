# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Cliente ( models.Model):
	nome=models.CharField(max_length=50)
	matricula=models.CharField(max_length=50)
	senha = models.CharField(max_length=50)

	def __str__(self):
		return self.nome



