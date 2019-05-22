from django.urls import path
from . import views

urlpatterns = [ path('upload/<int:pk>/', views.UploadData.as_view(), name='upload'),]
