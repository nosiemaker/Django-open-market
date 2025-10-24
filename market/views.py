from rest_framework import viewsets
from .models import Commodity, PriceRecord
from .serializers import CommoditySerializer, PriceRecordSerializer

class CommodityViewSet(viewsets.ModelViewSet):
    queryset = Commodity.objects.all()
    serializer_class = CommoditySerializer

class PriceRecordViewSet(viewsets.ModelViewSet):
    queryset = PriceRecord.objects.all()
    serializer_class = PriceRecordSerializer

