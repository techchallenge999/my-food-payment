from rest_framework import serializers

from api.apps.payment.models import Payment


class CreatePaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        all_fields = set(self.fields.keys())
        writable_field = {'value'}
        read_only_fields = all_fields - writable_field

        for field_name in read_only_fields:
            self.fields[field_name].read_only = True


class ListPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"


class UpdatePaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ["status"]
