from django.shortcuts import render, HttpResponse
# Create your views here.
from . models import Blog

def home(request):
    # return HttpResponse("Hello")
    blog = Blog.objects.all()

    context = {
        "blog":blog
    }
    return render(request, "home.html", context)

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")
