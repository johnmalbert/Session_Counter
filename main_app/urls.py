from django.urls import path     
from . import views

urlpatterns = [
    path('', views.some_function),
    path('destroy_session', views.destroy),
    path('2', views.add_two),
    path('amount', views.add_amount) 
]