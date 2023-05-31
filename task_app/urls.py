from django.urls import path
from . import views


urlpatterns = [
    path('',views.home_page_render, name="home_page"),
    path('details/<int:id>/',views.view_details, name = 'details'),
    path('list_view/',views.list_view, name="list_page"),
    
]
