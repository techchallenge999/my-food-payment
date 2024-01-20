from django.urls import path

from api.apps.payment.views import CreatePayment, ListPayment, UpdatePayment


urlpatterns = [
    path("create/", CreatePayment.as_view(), name="create"),
    path("list/", ListPayment.as_view(), name="list"),
    path("update/<uuid:uuid>", UpdatePayment.as_view(), name="update"),
]
