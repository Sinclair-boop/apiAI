from django.db import models


class Utilisateur(models.Model):
    nom = models.CharField(max_length=100)
    solde = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)



    # Ajoutez d'autres champs utilisateur si nécessaire

    def __str__(self):
        return self.nom


# class Transaction(models.Model):
#     utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
#     montant = models.DecimalField(max_digits=10, decimal_places=2)
#     date = models.DateField(auto_now_add=True)
#
#     # Ajoutez d'autres champs de transaction si nécessaire
#
#     def __str__(self):
#         return f"Transaction {self.id} de {self.utilisateur}"
