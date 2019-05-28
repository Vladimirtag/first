"""django_erp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from comp_control import views
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/', views.inbase, name = 'add'),#добавляем из .csv
    path('bomlist/<slug:bom_name>/', views.specification, name = "bomlist"), #покажет список компонентов для конкретного BOM
    path('erp/', TemplateView.as_view(template_name='index.html')),
    # path('groups/', views.checkform, name = 'bom'),
    # path('bomlist/', views.get_boms, name = 'boms'),
    path('index/', views.forma, name = "forma"),
    #умножаем
    path('bomlist/<slug:device>/<slug:multiple>/', views.countspecification, name = "countbomlist"), #покажет список компонентов 
    # path('jsres/', views.jsres, name = "jsres"),

    # path('writeoff/', views.writeoff, name = 'writeoff'),
    # path('writeofcomponent/<int:multiplier>/', views.get_boms, name = 'writeofcomponent'),
    # path('writeogroup/<int:multiplier>/', views.get_boms, name = 'writeofgroup'),

]
