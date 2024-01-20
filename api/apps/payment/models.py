from enum import Enum
import uuid

from django.db import models

from api.shared.mixins import TimestampMixin


class PaymentStatus(Enum):
    PENDING = "pendente"
    PAID = "pago"
    REFUSED = "recusado"


class Payment(TimestampMixin):
    value = models.CharField(max_length=7)
    status = models.CharField(
        max_length=50,
        choices=[(status.value, status.value) for status in PaymentStatus],
        default=PaymentStatus.PENDING.value,
    )
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
