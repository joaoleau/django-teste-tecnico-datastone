from django.urls import path
from .views import CurrencyView, CodesCurrencyView


urlpatterns = [
    path(
        "", CurrencyView.as_view(), name="currency-view"
    ),  # Endpoint para fazer as conversões
    path(
        "codes/", CodesCurrencyView.as_view(), name="currency-codes-view"
    ),  # Endpoint para ver as moedas suportadas
]
