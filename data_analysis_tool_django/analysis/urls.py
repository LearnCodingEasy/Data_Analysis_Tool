from django.urls import path
from .views import SalesDataAPIView

urlpatterns = [
    path('api/sales/', SalesDataAPIView.as_view(), name='sales-data')
]
