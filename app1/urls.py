
from django.urls import path
from .views import hello,about,contact

urlpatterns = [
    path('',hello,name='home'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact')
]
