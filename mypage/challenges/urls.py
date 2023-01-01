from django.contrib import admin
from django.urls import path
from challenges import views

admin.site.site_header = "Deepak IceCream Admin"
admin.site.site_title = "Deepak IceCream Admin Portal"
admin.site.index_title = "Welcome to Deepak IceCream"

urlpatterns = [
    path("", views.index, name="challenges"),
    path("about", views.about, name="about"),
    path("services", views.services, name="services"),
    path("contacts", views.contacts, name="contacts")
]
