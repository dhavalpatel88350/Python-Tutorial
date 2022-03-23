from django.http import HttpResponse
from django.shortcuts import render
from .models import Author,Entry

# Create your views here.
def hello(request): 
    a=Author.objects.all()
    b=Entry.objects.all()
    return render(request,'index.html',{'xyz':a,'abc':b})

def contact(request):
    return render(request,'contact.html')

def about(request):
    return HttpResponse("hello about")