
from django.contrib import admin
from django.urls import path,include
from triplet import views
urlpatterns = [
    path('',views.home,name="home"),
    path('api',views.index,name='api'),
]
