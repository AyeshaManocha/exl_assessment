# sales_analysis_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sales/', include('sales_analysis_app.urls')),
]
