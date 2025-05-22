from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as accounts_views

app_name = 'accounts'

urlpatterns = [
    path('register/', accounts_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='homepage'), name='logout'),
    path('profile/', accounts_views.profile, name='profile'),
    path('edit_profile/', accounts_views.edit_profile, name='edit_profile'),
    path('', accounts_views.login_view, name='accounts_root'), # Leite /accounts/ zur Login-Seite weiter (Beispiel)
]