from django.urls import path
from .views import *

app_name = 'hotels'

urlpatterns = [
    path('home/', home_page_view, name='home'),
]