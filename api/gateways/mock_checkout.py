from api.gateways.checkout_interface import (
    PaymentGatewayInterface,
    PaymentGatewayOutputDto,
)


class PaymentGateway(PaymentGatewayInterface):
    def create(self, payment_gateway_input_dto):
        return PaymentGatewayOutputDto(
            uuid=payment_gateway_input_dto.uuid, qr_data="mocked-qr-data"
        )
