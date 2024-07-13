from django.contrib import admin
from django.urls import path
from waterpotability import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('predict/', views.predict, name='predict'),
]