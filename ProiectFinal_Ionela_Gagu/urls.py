"""
URL configuration for ProiectFinal_Ionela_Gagu project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
import SmartShopping
from SmartShopping import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', SmartShopping.views.homepage, name="homepage"),
    path('delete/<int:id_item>', SmartShopping.views.delete_item, name='delete_item'),
    path('delete/confirm/<int:id_item>', SmartShopping.views.confirm_delete_item, name='confirm_delete_item'),
    path('adauga', SmartShopping.views.adauga_item, name='adauga_item'),
    path('marcheaza_ca_achizitionat/<int:id_item>', SmartShopping.views.marcheaza_ca_achizitionat, name='marcheaza_ca_achizitionat'),
    path('confirm_marcheaza_ca_achizitionat/<int:id_item>', SmartShopping.views.confirm_marcheaza_ca_achizitionat, name='confirm_marcheaza_ca_achizitionat'),
    path('get_nutritional_facts/<int:id_item>', SmartShopping.views.get_nutritional_facts, name="get_nutritional_facts"),
    path('not_found', SmartShopping.views.get_nutritional_facts, name="not_found")
]
