from django.urls import path
from home import views

urlpatterns = [
    path('modelo/', views.modelo)
]