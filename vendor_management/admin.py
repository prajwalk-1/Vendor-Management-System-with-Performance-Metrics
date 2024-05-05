from django.contrib import admin
from .models import Vendor, PurchaseOrder, HistoricalPerformance

# Register your models here.
class VendorAdmin(admin.ModelAdmin):
    list_display = ['name', 'vendor_code', 'on_time_delivery_rate', 'quality_rating_avg', 'fulfillment_rate']
    list_filter = ['on_time_delivery_rate', 'fulfillment_rate']
    search_fields = ['name', 'vendor_code']

admin.site.register(Vendor, VendorAdmin)

class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ['po_number', 'vendor', 'order_date', 'delivery_date', 'status']
    list_filter = ['status', 'delivery_date']
    search_fields = ['po_number', 'vendor__name']

admin.site.register(PurchaseOrder, PurchaseOrderAdmin)

class HistoricalPerformanceAdmin(admin.ModelAdmin):
    list_display = ['vendor', 'date', 'on_time_delivery_rate', 'quality_rating_avg', 'average_response_time', 'fulfillment_rate']
    list_filter = ['vendor']
    search_fields = ['vendor__name']

admin.site.register(HistoricalPerformance, HistoricalPerformanceAdmin)