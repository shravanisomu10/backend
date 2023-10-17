from django.urls import include, path

from . import views
from .views import doctor_list, doctor_detail, doctor_list_create

urlpatterns = [
    path('doctors/', doctor_list, name='doctor-list'),
    path('doctors/<int:pk>/', doctor_detail, name='doctor-detail'),
    path('api/doctors/', views.get_doctors, name='get_doctors'),
       path('doctors/', doctor_list_create, name='doctor-list-create'),

    #path('doctors/', include('doctor.urls')),
]
  