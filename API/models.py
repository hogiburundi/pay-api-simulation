from django.db import models
from django.utils import timezone

# Create your models here.

class InfoTransaction(models.Model):
	"""docstring for InfoTransaction"""
	nom = models.CharField()
	prenom = models.CharField()
	date = models.DateField(default=timezone.now)
	source = models.CharField()
	destination = models.CharField()
	montant = models.CharField()
	objet = models.CharField()
	serie = models.CharField()