from datetime import datetime  
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Appointment
from .serializers import AppointmentSerializer
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse

@api_view(['GET', 'POST'])
#@permission_classes([IsAuthenticated])

def appointment_list(request):
    if request.method == 'GET':
        appointments = Appointment.objects.all()
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def appointment_detail(request, pk):
    try:
        appointment = Appointment.objects.get(pk=pk)
    except Appointment.DoesNotExist:
        return Response({'message': 'Appointment not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AppointmentSerializer(appointment)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AppointmentSerializer(appointment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        appointment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
def get_appointments(request):
    appointments = Appointment.objects.all()
    data = [
        {
            'id': appointment.id,
            'first_name': appointment.first_name,
            'last_name': appointment.last_name,
            'dob': appointment.dob,
            'doctors_name': appointment.doctors_name,
            'date': appointment.date,
        }
        for appointment in appointments
    ]
    return JsonResponse(data, safe=False)
@api_view(['POST'])
def cancel_appointment(request, pk):
    try:
        appointment = Appointment.objects.get(pk=pk)
        appointment.status = 'canceled'  
        appointment.save()
        return Response({'message': 'Appointment canceled successfully'})
    except Appointment.DoesNotExist:
        return Response({'message': 'Appointment not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def edit_appointment(request, pk):
    try:
        appointment = Appointment.objects.get(pk=pk)
    except Appointment.DoesNotExist:
        return Response({'message': 'Appointment not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = AppointmentSerializer(appointment, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def reschedule_appointment(request, pk):
    if request.method == 'POST':
        try:
            appointment = get_object_or_404(Appointment, pk=pk)
            new_datetime = request.data.get('new_datetime')
            
            new_datetime = datetime.strptime(new_datetime, '%Y-%m-%d %H:%M')
         
            appointment.date = new_datetime
            appointment.save()  
            return JsonResponse({'message': 'Appointment rescheduled successfully', 'new_datetime': new_datetime}, status=200)
        except Exception as e:
            return JsonResponse({'error': f'Failed to reschedule appointment: {str(e)}'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
    
@api_view(['PUT'])
def update_appointment(request, pk):
    if request.method == 'PUT':
        try:
            appointment = get_object_or_404(Appointment, pk=pk)
            
          
            print(request.data.get('first_name'))
            new_first_name = request.data.get('first_name')
            new_last_name = request.data.get('last_name')
            new_doctors_name = request.data.get('doctors_name')
            new_appointment_date = request.data.get('appointment_date')


            #return JsonResponse({'test':new_first_name},200)
            
            
            appointment.first_name = new_first_name
            appointment.last_name = new_last_name
            appointment.doctors_name = new_doctors_name
            appointment.date = new_appointment_date
            
            appointment.save()  
            
            return JsonResponse({'message': 'Appointment updated successfully', 'new_first_name': new_first_name, 'new_last_name': new_last_name, 'new_doctors_name': new_doctors_name, 'new_appointment_date': new_appointment_date}, status=200)
        except Exception as e:
            return JsonResponse({'error': f'Failed to update appointment: {str(e)}'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)

    

    
