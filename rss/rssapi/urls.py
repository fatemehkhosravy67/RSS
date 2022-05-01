from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('news/', views.RSSView.as_view(), name='news'),
]
