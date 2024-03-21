from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CurrencySerializer
from .services import CurrencyService
from django.urls import reverse


class CurrencyView(APIView):
    services = CurrencyService()
    serializer_class = CurrencySerializer

    def get(self, request) -> Response:
        if (
            not request.query_params
        ):  # Verifica se o usuário não passou nenhum parametro
            data = {
                "error": "To make the request, please use a query string with the following format: api/?from=BRL&amount=10&to=USD",
                "links": {
                    "ref": "currency-codes-view",
                    "href": reverse("currency-codes-view"),
                },
            }
            return Response(data=data)

        serializer = self.serializer_class(
            data=request.query_params
        )  # Valida a formatação dos parametros passados usando o CurrencySerialzier
        if serializer.is_valid(raise_exception=True):
            data = serializer.validated_data
            data["result"] = (
                self.services.currency(  # Acrescente em 'data' uma nova chave 'result' com o valor da conversão
                    param_from=data.get("from"),
                    amount=data.get("amount"),
                    to=data.get("to"),
                )
            )
            return Response(data=data)

        return Response(
            serializer.errors
        )  # Caso os parametros estejam num formato incorreto


class CodesCurrencyView(APIView):
    services = CurrencyService()

    def get(self, request) -> Response:
        data = {}
        data["codes"] = (
            self.services.codes_currency()
        )  # Acrescenta em data a chave 'codes' com os códigos das moedas suportadas
        return Response(data=data)
