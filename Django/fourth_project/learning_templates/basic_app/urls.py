from django.urls import path
from basic_app import views


# this is for template tagging
app_name = 'basic_app' # this is going to say see under the basic_app and take the URL that matches

urlpatterns = [
    path('relative/', views.relative, name = 'relative'),
    path('other/', views.other, name = 'other'),
]