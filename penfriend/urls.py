from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('registration/', views.UserCreateView.as_view(), name='registration'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('profile/<int:pk>', views.ProfileUpdateView.as_view(), name='profile'),
]
