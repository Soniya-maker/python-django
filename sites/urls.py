from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('dalhart_site', views.dalhart_site),
    path('hilmar_site', views.hilmar_site),
    path('dodge_site', views.dodge_site),
    path('milk_receiving', views.milk_receiving),
    path('plant_5', views.plant_5),
    path('plant_6', views.plant_6),
    path('protein', views.protein),
    path('dryer', views.dryer),
    path('permeate', views.permeate),
    path('chart', views.show_chart),
    path('future_site', views.future_site),
]