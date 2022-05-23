"""hw URL Configuration

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
from hw import views

urlpatterns = [
    path('login',views.login),
    path('admin/', admin.site.urls),
    path('get_data',views.get_data),
    path('insert_data',views.insert_data),
    path('del_data',views.del_data),
    path('get_ship_data',views.get_ship_data),
    path('get_shipname',views.get_shipname),
    path('del_ship_data',views.del_ship_data),
    path('post_ship_data',views.post_ship_data),
    path('insert_ship_data',views.insert_ship_data),
    path('post_inbei_data',views.post_inbei_data),
    path('del_inbei_data',views.del_inbei_data),
    path('insert_inbei_data',views.insert_inbei_data),
    path('post_outbei_data', views.post_outbei_data),
    path('del_outbei_data', views.del_outbei_data),
    path('insert_outbei_data', views.insert_outbei_data),
    # path('get_cargo_data',views.get_cargo_data),
    path('post_incargo_data',views.post_incargo_data),
    path('del_incargo_data',views.del_incargo_data),
    path('insert_incargo_data',views.insert_incargo_data),
    path('post_outcargo_data', views.post_outcargo_data),
    path('del_outcargo_data', views.del_outcargo_data),
    path('insert_outcargo_data', views.insert_outcargo_data),
    path('get_in_file',views.get_in_file),
    path('get_out_file',views.get_out_file),
    path('export_file_data',views.export_file_data),
    path('get_in_file_data',views.get_in_file_data),
    path('get_out_file_data',views.get_out_file_data),
    path('get_ship_data',views.get_ship_data),
    path('post_invis_data',views.post_invis_data),
    path('post_outvis_data',views.post_outvis_data),
    path('set_insch_data',views.set_insch_data),
    path('post_insce_data',views.post_insce_data),
    path('del_insce_data',views.del_insce_data),
    path('set_outsch_data', views.set_outsch_data),
    path('post_outsce_data', views.post_outsce_data),
    path('del_outsce_data', views.del_outsce_data),
    path('post_plan_data',views.post_plan_data),
    path('export_plan_data',views.export_plan_data)
]
