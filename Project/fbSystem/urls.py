from django.urls import path
from . import views

urlpatterns = [
    path('feedback/success/', views.feedback_success, name='feedback_success'),
]
