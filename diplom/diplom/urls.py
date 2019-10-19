"""diplom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from app.views import signup, home, phone, section, basket, accessories
from django.contrib.auth.views import LoginView, LogoutView


# class MyLoginView(LoginView):
#     template_name = 'login.html'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accessories', accessories, name='accessories'),
    path('', home, name='main'),
    path('section/phone/', phone, name='phone'),
    path('section/', section, name='section'),
    path('section/cart/', basket, name='cart'),
    path('signup/', signup, name='signup'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
