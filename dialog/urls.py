from django.urls import path

from . import views


urlpatterns = [
    path('', views.dialog_index, name='dialog_index')
]
