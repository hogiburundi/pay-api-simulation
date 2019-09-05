from django.db import models
from django.utils import timezone

# Create your models here.

class InfoTransaction(models.Model):
	"""docstring for InfoTransaction"""
	nom = models.CharField(max_length=30)
	prenom = models.CharField(max_length=30)
	date = models.DateField(default=timezone.now)
	source = models.CharField(max_length=30)
	destination = models.CharField(max_length=30)
	montant = models.CharField(max_length=30)
	objet = models.CharField(max_length=30)
	serie = models.CharField(max_length=30)