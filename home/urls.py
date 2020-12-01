from django.contrib import admin
from django.urls import path
from home import views

admin.site.site_header = "FLORA STORE Admin"
admin.site.site_title = "FloraStore Admin Portal"
admin.site.index_title = "Welcome to Flora Store"

urlpatterns = [
    path('', views.index, name = 'home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('icecream', views.icecream, name='icecream'),
    path('vegHome', views.vegHome, name='vegHome')

]
