from django.shortcuts import render

# Create your views here.

def list_posts(request):
    return render(request,'index.html')

def aboutme(request):
    return render(request,'aboutme.html')