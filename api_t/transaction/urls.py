from django.urls import path
from . import views
from .views import Predict

urlpatterns = [
    # path('predict/', views.predict, name='predict'),
    # path('ma-vue/', predict, name='ma-vue'),
    path('model/', Predict.as_view(), name='prediction'),
]