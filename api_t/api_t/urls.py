# monprojet/urls.py
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
# from transaction.views import UtilisateurViewSet, UtilisateurViewSetRetrait, UtilisateurViewSetDepot

# from api_t import transaction

# router = routers.DefaultRouter()
# router.register(r'utilisateurs', UtilisateurViewSet)
# router.register(r'utilisateurs/utilisateur', UtilisateurViewSet)
# router.register(r'utilisateurs/utilisateur/retrait', UtilisateurViewSetRetrait)
# router.register(r'utilisateurs/utilisateur/depot', UtilisateurViewSetDepot)
# router.register(r'utilisateurs/utilisateur/<int:id>/depot', UtilisateurViewSetDepot)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include(router.urls)),
    path("pre/", include("transaction.urls")),
    # path('ma-vue/', Prediction.as_view(), name='ma-vue'),
]
