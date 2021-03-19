from core import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('contact/', views.contact, name="contact"),
    path('serv/', include('serv.urls')),
    path('edu/', include('edu.urls')),
]
