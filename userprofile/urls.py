
from django.urls import path
from .import views as v

app_name = "userprofile"

urlpatterns = [
    path('register_user/', v.register_user, name="register"),
    path('login_user/', v.login_view, name="login"),
    path('logout_user/', v.logout_view, name="logout"),
]
