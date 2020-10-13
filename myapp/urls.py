from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('myapp/', views.my_view),

]
