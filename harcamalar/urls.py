from django.urls import path
from . import views

urlpatterns = (
    path('harcama_ekle/', views.harcama_ekle, name='harcama_ekle'),
)
