from django.urls import path
from AppTwo import views


##urlpatterns = [
  ##  path('',views.help, name = 'help'),]

urlpatterns = [
    path('',views.users, name = 'users'),]