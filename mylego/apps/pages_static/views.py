from django.shortcuts import render

def index(request):
    return render(request, 'pages_static/index.html')