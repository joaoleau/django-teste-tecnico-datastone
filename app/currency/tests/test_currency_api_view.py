import pytest
from django.urls import reverse
from decouple import config
import requests

APIKEY = config("APIKEY")


@pytest.fixture
def query_params():
    params = {"from": "BRL", "amount": 200, "to": "USD"}
    return params


def test_endpoint_of_quotations():
    url = f"https://api.currencyfreaks.com/v2.0/rates/latest?apikey={APIKEY}&symbols=BRL,USD"
    response = requests.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_currency_api_view_return_status_code_200(query_params, client):
    url = reverse("currency-view")
    response = client.get(url, data=query_params)
    assert response.status_code == 200


@pytest.mark.django_db
def test_codes_currency_api_view_return_status_code_200(query_params, client):
    url = reverse("currency-codes-view")
    response = client.get(url, data=query_params)
    assert response.status_code == 200


@pytest.mark.django_db
def test_currency_api_view_return_json(query_params, client):
    url = reverse("currency-view")
    response = client.get(url, data=query_params)
    assert response.headers["content-type"] == "application/json"


@pytest.mark.parametrize(
    "param_from, to, amount, expected_status_code",
    [("BRL", 200, "TUC", 400), ("BTC", "BRL", 1, 200)],
)
def test_currency_api_view_return_status_code_correct(
    client, param_from, to, amount, expected_status_code
):
    params = {"from": param_from, "amount": amount, "to": to}
    url = reverse("currency-view")
    response = client.get(url, data=params)
    assert response.status_code == expected_status_code
