from rest_framework.urls import path
from .views import MerchantDetailView


urlpatterns = [
    path('merchants/<int:pk>/', MerchantDetailView.as_view(), name="merchant-detail")
]