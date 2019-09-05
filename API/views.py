from django.shortcuts import HttpResponse
from json import dumps as jsonify
from .models import InfoTransaction

def check(request, id_transaction):
    transaction = InfoTransaction.objects.get(serie=id_transaction)

    if transaction:
        data = {
			"nom" : transaction.nom,
			"prenom" : transaction.prenom,
			"date" : transaction.date,
			"source" : transaction.source,
			"destination" : transaction.destination,
			"montant" : transaction.montant,
			"objet" : transaction.objet,
			"serie" : transaction.serie,
        }
        utilisateur.append(data)
        json = jsonify(utilisateur)
        return HttpResponse(json , content_type="application/json")
    return HttpResponse(None, content_type="application/json")


