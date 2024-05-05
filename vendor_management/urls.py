from django.urls import path
from .views import (
    VendorListCreate,
    VendorRetrieveUpdateDestroy,
    PurchaseOrderListCreate,
    PurchaseOrderRetrieveUpdateDestroy,
)

urlpatterns = [
    path('vendors/', VendorListCreate.as_view(), name='vendor-list-create'),
    path('vendors/<int:pk>/', VendorRetrieveUpdateDestroy.as_view(), name='vendor-retrieve-update-destroy'),
    path('purchase_orders/', PurchaseOrderListCreate.as_view(), name='purchaseorder-list-create'),
    path('purchase_orders/<int:pk>/', PurchaseOrderRetrieveUpdateDestroy.as_view(), name='purchaseorder-retrieve-update-destroy'),
]
