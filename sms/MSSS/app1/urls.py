from django.urls import path
from .views import contact,index,about,contact,signin,signup

urlpatterns = [
    path('',index,name='home'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('signin/',signin,name='sign-in'),
    path('signup/',signup,name='sign-up'),
]