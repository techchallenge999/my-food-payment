from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/payment/', include(('api.apps.payment.urls', 'payment'), namespace='api.apps.payment')),
]
