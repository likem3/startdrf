from rest_framework import generics
from .models import Merchant
from .serializers import MerchantSerializer
from app.utils.permissions import IsMerchant


class MerchantDetailView(generics.RetrieveAPIView):
    queryset = Merchant.objects.all()
    permission_classes = [IsMerchant]
    serializer_class = MerchantSerializer
