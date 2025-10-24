from django.contrib import admin
from .models import Commodity, PriceRecord

@admin.register(Commodity)
class CommodityAdmin(admin.ModelAdmin):
    list_display = ('name', 'unit')

@admin.register(PriceRecord)
class PriceRecordAdmin(admin.ModelAdmin):
    list_display = ('commodity', 'date', 'price')
    list_filter = ('commodity', 'date')
