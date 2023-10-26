from django.urls import path
from . import views


app_name = 'Technologies'
urlpatterns = [
    path('', views.technologies, name='technologies'),
]