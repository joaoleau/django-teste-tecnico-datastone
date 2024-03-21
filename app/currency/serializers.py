from rest_framework import serializers, exceptions
from django.utils.translation import gettext_lazy as _


class CurrencySerializer(serializers.Serializer):
    param_from = serializers.CharField(  #'param_from' foi escolhido pois 'from' é uma palavra reservada
        min_length=1,
    )
    to = serializers.CharField(min_length=1)
    amount = serializers.FloatField()

    def validate_amount(self, value):
        if value < 0:
            raise exceptions.ValidationError(
                _("The value of 'amount' must be a positive number.")
            )
        return value

    def get_fields(self):
        fields = super().get_fields()
        fields["from"] = fields.pop(
            "param_from"
        )  # Aqui é renomeado o field 'param_from' para 'from'
        fields = {
            "from": fields.pop("from"),
            **fields,
        }  # Ordena-se a fim de manter a ordem exigida
        return fields
