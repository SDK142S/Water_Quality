from django.urls import path
from . import views

app_name = 'waterpotability'

urlpatterns = [
    path('', views.index, name='index'),  # Make sure 'index' is defined here
    path('predict/', views.predict, name='predict'),
    # Other URL patterns as needed
]
