"""gymnation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from pages.views import get_about_page, get_our_team_page, get_classes_page, get_contact_us_page, get_shop_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_about_page, name='get_about_page'),
    path('our-team/', get_our_team_page, name='get_our_team_page'),
    path('classes/', get_classes_page, name='get_classes_page'),
    path('contact-us/', get_contact_us_page, name='get_contact_us_page'),
    path('shop/', get_shop_page, name='get_shop_page')
]
