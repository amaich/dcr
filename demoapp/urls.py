from django.urls import path

from .views import *

urlpatterns = [
    path('', main),
    path('list/', test_list)
]
