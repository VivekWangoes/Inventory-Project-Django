from django.urls import path
from .views import *

urlpatterns = [
    path("", Registration.as_view(), name="registration"),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogOut.as_view(), name="logout")
]