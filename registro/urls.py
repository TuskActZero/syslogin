from django.urls import path
from .views import Home, Registro, LoginPage
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', Home.as_view(), name="index"),
    path('accounts/singup', Registro.as_view(), name="registro"),
    path('accounts/login', LoginPage.as_view(), name="login"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)