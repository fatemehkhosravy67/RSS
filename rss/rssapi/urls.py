from django.urls import path
from . import views

urlpatterns = [
    path('news/', views.RSSView.as_view(), name='news'),
]
