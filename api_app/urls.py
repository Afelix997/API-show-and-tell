from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("<int:image_id>", views.index, name="page2"),  
]