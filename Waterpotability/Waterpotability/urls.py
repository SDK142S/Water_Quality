from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Correct way to include admin URLs
    path('', include('waterpotability.urls')),
]
