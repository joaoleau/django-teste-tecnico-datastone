import pytest
from currency.serializers import CurrencySerializer


@pytest.mark.parametrize("param_from, to, amount", [("BRL", "USD", 10)])
def test_currency_serializer(param_from, to, amount):
    data = {"from": param_from, "to": to, "amount": amount}
    serializer = CurrencySerializer(data=data)
    serializer_is_valid = serializer.is_valid()
    assert serializer_is_valid is True
