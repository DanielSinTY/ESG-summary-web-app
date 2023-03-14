from django.urls import path
from . import views

urlpatterns = [
    path('company/',views.selected),
    path('',views.search)
]