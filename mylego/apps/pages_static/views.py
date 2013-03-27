from django.shortcuts import render

def index(request):
    return render(request, 'pages_static/index.html')

def contact(request):
    return render(request, 'pages_static/contact.html')

def construction(request):
    return render(request, 'pages_static/construction.html')