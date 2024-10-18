from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import expense_create, custom_logout #,debug_expenses
from .forms import CustomLoginForm

urlpatterns = [
    path('time/', views.current_time, name='current_time'),
    path('login/', LoginView.as_view(
        template_name='expenses/login.html',
        authentication_form=CustomLoginForm,
        redirect_authenticated_user=True
    ), name='giris'),
    path('logout/', custom_logout, name='logout'),
    path(' expenses/', expense_create, name='expense_create'),  # Changed from 'expense/create/'
    path('', expense_create, name='home'),
    # path('debug/', debug_expenses, name='debug_expenses'),
]
