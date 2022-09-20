from email.policy import HTTP
from django.shortcuts import render
from rest_framework.response import Response
from flightApp.serializers import PassengerSerializer,ReservationSerializer,FlightSerializer
from rest_framework import status
from flightApp.models import Flight,Passenger,Reservation
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['POST'])
def save_reservation(request):
    flight = Flight.objects.get(id=request.data['id'])

    passenger=Passenger()
    passenger.firstName=request.data['firstName']
    passenger.lastName=request.data['lastName']
    passenger.middleName=request.data['middleName']
    passenger.email=request.data['email']
    passenger.phone=request.data['phone']
    passenger.save()

    reservaion=Reservation()
    reservaion.flight=flight    
    reservaion.passenger=passenger
    reservaion.save()
    return Response(status=status.HTTP_201_CREATED)


@api_view(['GET','POST'])
def flights_list(request):
    if request.method=='GET':
        flights=Flight.objects.all()
        serializer=FlightSerializer(flights,many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer=FlightSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    


@api_view(['GET','PUT','DELETE'])
def flight_details(request,pk):
    try:
        flight=Flight.objects.get(pk=pk)
    except Flight.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serializer = FlightSerializer(flight)
        return Response(serializer.data)

    elif request.method=='PUT':
        serializer = FlightSerializer(flight,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        flight.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET','POST'])
def passengers_list(request):
    if request.method=='GET':
        flights=Passenger.objects.all()
        serializer=PassengerSerializer(flights,many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer=PassengerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    


@api_view(['GET','PUT','DELETE'])
def passenger_details(request,pk):
    try:
        passenger=Passenger.objects.get(pk=pk)
    except Passenger.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serializer = PassengerSerializer(passenger)
        return Response(serializer.data)

    elif request.method=='PUT':
        serializer = PassengerSerializer(passenger,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        passenger.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
def reservations_list(request):
    if request.method=='GET':
        reservations=Reservation.objects.all()
        serializer=ReservationSerializer(reservations,many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer=ReservationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 

@api_view(['GET','PUT','DELETE'])
def reservation_details(request,pk):
    try:
        reservation=Reservation.objects.get(pk=pk)
    except Reservation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serializer = ReservationSerializer(reservation)
        return Response(serializer.data)

    elif request.method=='PUT':
        serializer = ReservationSerializer(reservation,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        reservation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

