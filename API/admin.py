from django.contrib import admin
from .models import *

class InfoTransactionAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'date', 'source', 'destination', 'montant', 'objet', 'serie')
    list_filter = ('nom', 'prenom', 'date', 'source', 'destination', 'montant', 'objet', 'serie')
    search_fields = ('nom', 'prenom', 'date', 'source', 'destination', 'montant', 'objet', 'serie')


admin.site.register(InfoTransaction, InfoTransactionAdmin)