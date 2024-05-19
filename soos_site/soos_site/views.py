from django.shortcuts import render

def base_view(request):
    # Render the base.html template
    return render(request, 'base.html')

def home_view(request):
    return render(request, 'home.html')