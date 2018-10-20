from django.urls import path, include

from .views import login, logout, signup

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('signup/', signup, name='signup'),
]
