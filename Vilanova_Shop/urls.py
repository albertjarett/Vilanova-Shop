"""
URL configuration for Vilanova_Shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from Productos.views import Productos, personalized_products
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('vila-admin', admin.site.urls),
    path('', Productos, name='product_list'),
    path('personalizados/', personalized_products, name='personalized_product_list'),
 
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
