from django.urls import path

from . import views


urlpatterns = [
    path('', views.DialogView.as_view(), name='dialog_view'),
]
