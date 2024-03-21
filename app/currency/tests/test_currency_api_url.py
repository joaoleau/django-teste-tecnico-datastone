from django.urls import reverse, resolve
import pytest
from currency import views


@pytest.mark.parametrize(
    "view_name, expeted_view",
    [
        ("currency-view", views.CurrencyView),
        ("currency-codes-view", views.CodesCurrencyView),
    ],
)
def test_url_resolves_to_expected_view(view_name, expeted_view):
    resp = resolve(reverse(view_name))
    resp_view_class = resp.func.view_class()
    assert resp_view_class.__class__ == expeted_view
