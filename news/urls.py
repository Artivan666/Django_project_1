from django.urls import path
from news.views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about),
    path('cats/<int:cat_id>/', category)
]