from django.urls import path
from cafeteria import views

urlpatterns = [
    path('', views.home,name='home'),
    path('cafe/',views.pedidos,name='pedidos')

]
