from django.shortcuts import render

# Create your views here.

def list_posts(request):
    return render(request,'index.html')