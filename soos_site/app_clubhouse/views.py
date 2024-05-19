from django.shortcuts import render

def clubhouse_home(request):
    return render(request, 'clubhouse.html')

def mancala(request):
    return render(request, 'clubhouse_mancala.html')

def dotsandboxes(request):
    return render(request, 'clubhouse_dotsandboxes.html')