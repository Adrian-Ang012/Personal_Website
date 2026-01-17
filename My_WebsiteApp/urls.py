from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page, name='home_page'),
    path("contact/", views.contact, name="contact"),
     path("contact/success/", views.contact_success, name="contact_success"),

]