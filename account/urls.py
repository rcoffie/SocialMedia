from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
  path('register/',views.signup,name='register'),
  path('login/',views.userlogin,name='login'),
  path('',views.dashboard,name='dashboard')
]
