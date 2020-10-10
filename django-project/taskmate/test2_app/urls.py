from django.urls import path
from test2_app import views
urlpatterns = [
    path('', views.test2 , name='test2'),
]
