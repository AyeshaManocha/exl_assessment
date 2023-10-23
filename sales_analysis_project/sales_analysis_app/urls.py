# sales_analysis_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_sales_data, name='upload_sales_data'),
    path('calculate/', views.calculate_metrics, name='calculate_metrics'),
]
