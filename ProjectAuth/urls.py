# url files for /auth authentication system


from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("login/", views.authLogin),
    path("employee/register/", views.authEmployeeRegister),
    path('change_password/', auth_views.PasswordChangeView.as_view(template_name='change_password.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),
]
