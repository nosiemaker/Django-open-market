from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CommodityViewSet, PriceRecordViewSet

router = DefaultRouter()
router.register('commodities', CommodityViewSet)
router.register('prices', PriceRecordViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
