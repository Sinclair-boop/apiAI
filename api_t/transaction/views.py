# transactions/views.py
from http import HTTPStatus
import os

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Utilisateur
from .serializers import UtilisateurSerializer
import pickle
import pandas as pd
from django.http import JsonResponse, HttpResponse


chemin_fichier = r"C:\Users\Sinclair\Desktop\UEProjet\api2\api_t\transaction\xgb_model2.pkl"
with open(chemin_fichier, 'rb') as file:
    model = pickle.load(file)

class Predict(APIView):
    def get(self, request):
        #recupere les parametres de la requete
        parametre = float(request.GET.get('oldsolde'))
        #logique de la vue representent les donnees
        dataSin = {'amount': [parametre]}
        # Conversion du dictionnaire en DataFrame
        dfsin = pd.DataFrame(dataSin)
        type(dfsin)

        # Faire une prédiction avec le modèle
        y_pred = model.predict(dfsin)
        print(y_pred)
        data = {'nom':request.GET.get('nom'),
                'telephone':request.GET.get('telephone'),
                'oldsolde':float(request.GET.get('oldsolde')),
                'date':request.GET.get('date'),
                'isfraud':y_pred[-1],
                }
        print(data)
        # Retourner la prédiction sous forme de dictionaire
        return Response(data)


# class UtilisateurViewSet(viewsets.ModelViewSet):
#     queryset = Utilisateur.objects.all()
#     serializer_class = UtilisateurSerializer
#
# class UtilisateurViewSetRetrait(viewsets.ModelViewSet):
#     queryset = Utilisateur.objects.all()
#     serializer_class = UtilisateurSerializer
#
# # PUT utilisateur/retrait/{id}/
#     def update(self, request, pk):
#
#         utilisateur = self.get_object()
#         montant = float(request.data["solde"])
#         solde = float(utilisateur.solde)
#         if montant is None:
#             return Response({'message': 'Le montant est requis.'}, status=status.HTTP_400_BAD_REQUEST)
#         if solde < montant:
#             return Response({'message': 'Fonds insuffisants.'}, status=status.HTTP_400_BAD_REQUEST)
#         solde -= montant
#         utilisateur.save()
#         result = {
#                 'nom': utilisateur.nom,
#                 f'nouveau solde': solde,
#         }
#         return Response(f"{result}", status=status.HTTP_201_CREATED)
#
# class UtilisateurViewSetDepot(viewsets.ModelViewSet):
#     queryset = Utilisateur.objects.all()
#     serializer_class = UtilisateurSerializer
# # PUT utilisateur/depot/{id}/
#     def update(self, request, pk):
#
#         utilisateur = self.get_object()
#         montant = float(request.data["solde"])
#         solde = float(utilisateur.solde)
#         if montant is None:
#             return Response({'message': 'Le montant est requis.'}, status=status.HTTP_400_BAD_REQUEST)
#         solde += montant
#         utilisateur.save()
#         result = {
#                 'nom': utilisateur.nom,
#                 f'nouveau solde': solde,
#         }
#         return Response(f"{result}", status=status.HTTP_201_CREATED)
