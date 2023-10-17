from django.urls import path
from . import views
from .views import get_appointments

urlpatterns = [
    path('appointments/', views.appointment_list, name='appointment-list'),
    path('appointments/<int:pk>/', views.appointment_detail, name='appointment-detail'),
     path('api/appointments/', get_appointments, name='get_appointments'),
     path('api/appointments/cancel/<int:pk>/', views.cancel_appointment, name='cancel-appointment'),
    path('appointment/api/appointments/edit/<int:pk>/', views.edit_appointment, name='edit-appointment'),
 path('api/appointments/update/<int:pk>/', views.update_appointment, name='update-appointment'),

   
  path('api/appointments/reschedule/<int:pk>/', views.reschedule_appointment, name='reschedule-appointment')


     
]
