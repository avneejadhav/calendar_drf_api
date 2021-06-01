from django.urls import path
from . import views


urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('appointment-list/', views.appointmentList, name="appointment-list"),
    path('appointment-detail/<str:pk>/', views.appointmentDetail, name="appointment-Detail"),
    path('appointment-create/', views.appointmentCreate, name="appointment-Create"),
    path('appointment-update/<str:pk>/', views.appointmentUpdate, name="appointment-update"),
    path('appointment-delete/<str:pk>/', views.appointmentDelete, name="appointment-delete"),
]