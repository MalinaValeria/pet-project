from django.urls import path

from shop import views

urlpatterns = [
    path('', views.MainPageView.as_view(), name='index'),
    ]