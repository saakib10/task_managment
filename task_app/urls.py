from django.urls import path
from . import views


urlpatterns = [
    path('',views.home_page_render, name="home_page")
]
