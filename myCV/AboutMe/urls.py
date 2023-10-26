from django.urls import path
from . import views


app_name = 'AboutMe'
urlpatterns = [
    path('', views.aboutMe, name='aboutMe')
]
