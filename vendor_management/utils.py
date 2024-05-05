from django.db.models import Count, Avg
from django.utils import timezone

def calculate_performance_metrics(vendor):
    total_completed_orders = vendor.purchase_orders.filter(status='completed').count()
    if total_completed_orders > 0:
        vendor.on_time_delivery_rate = vendor.purchase_orders.filter(status='completed', delivery_date__lte=timezone.now()).count() / total_completed_orders
        vendor.quality_rating_avg = vendor.purchase_orders.filter(status='completed').aggregate(avg_rating=Avg('quality_rating'))['avg_rating']
        vendor.average_response_time = vendor.purchase_orders.filter(status='completed', acknowledgment_date__isnull=False).aggregate(avg_response=Avg('acknowledgment_date' - 'issue_date'))['avg_response']
        vendor.fulfillment_rate = vendor.purchase_orders.filter(status='completed').count() / vendor.purchase_orders.count()
    else:
        vendor.on_time_delivery_rate = 0
        vendor.quality_rating_avg = 0
        vendor.average_response_time = 0
        vendor.fulfillment_rate = 0
    vendor.save()
