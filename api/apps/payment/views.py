import os
import uuid

from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response

from api.gateways.mock_checkout import PaymentGateway
from api.gateways.checkout_interface import PaymentGatewayInputDto
from api.apps.payment.models import Payment
from api.apps.payment.serializers import CreatePaymentSerializer, ListPaymentSerializer


class CreatePayment(CreateAPIView):
    serializer_class = CreatePaymentSerializer
    queryset = Payment.objects.all()

    def post(self, request, *args, **kwargs):
        webhook_base_url = os.getenv("API_URL", "http://localhost:8000")
        new_payment_uuid = str(uuid.uuid4())
        qr_data = PaymentGateway().create(
            PaymentGatewayInputDto(
                uuid=new_payment_uuid,
                notification_url=f"{webhook_base_url}/webhook/{new_payment_uuid}",
                total_amount=request.data.get('value'),
            )
        ).qr_data

        serializer = self.get_serializer(data={
            'value': request.data.get('value'),
            'uuid': new_payment_uuid,
            'qr_data': qr_data,
        })
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        response_data = serializer.data
        response_data["qr_data"] = qr_data
        return Response(
            response_data,
            status=status.HTTP_201_CREATED,
        )


class ListPayment(ListAPIView):
    serializer_class = ListPaymentSerializer
    queryset = Payment.objects.all()
