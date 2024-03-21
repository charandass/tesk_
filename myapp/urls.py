from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_list),
    path('create_bill/', views.create_bill),
    path('bills/<int:bill_id>', views.bill_detail, name="bill_detail")
    
]