from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    re_path(r'^add/', views.add, name="add"),
    path('car/<int:id>/', views.detail),
]
