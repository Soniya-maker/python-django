from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def dalhart_site(request):
    return render(request, "dalhart-site.html")

def hilmar_site(request):
    return render(request, "hilmar-site.html")

def dodge_site(request):
    return render(request, "dodge-site.html")

def milk_receiving(request):
    return render(request, "milk_receiving.html")

def plant_5(request):
    return render(request, "plant_5.html")

def plant_6(request):
    return render(request, "plant_6.html")

def protein(request):
    return render(request, "protein.html")

def dryer(request):
    return render(request, "dryer.html")

def permeate(request):
    return render(request, "permeate.html")

def show_chart(request):
    return render(request, "chart.html")

def future_site(request):
    return render(request, "future_site.html")