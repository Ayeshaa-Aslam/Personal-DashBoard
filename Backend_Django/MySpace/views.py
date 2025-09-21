from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer
from .models import Note
from .serializers import NoteSerializer
import requests
from django.conf import settings

@api_view(['GET', 'PUT'])
def profile_view(request):
    profile, created = Profile.objects.get_or_create(id=1)  # single profile only
    
    if request.method == 'GET':
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
@api_view(['GET', 'POST'])
def note_view(request):
    note, created = Note.objects.get_or_create(id=1) 
    
    if request.method == 'GET':
        serializer = NoteSerializer(note)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = NoteSerializer(note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

@api_view(['GET'])
def weather_view(request):
    city = request.GET.get("city", "Lahore")
    api_key = "4e1d0768a90083b46f74647c56e697d4" 
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    r = requests.get(url)
    data = r.json()
    
    return Response({
        "city": data["name"],
        "temp": data["main"]["temp"],
        "condition": data["weather"][0]["description"],
        "icon": data["weather"][0]["icon"],
    })

@api_view(['GET'])
def quote_view(request):
    url = "https://zenquotes.io/api/random"
    r = requests.get(url)
    data = r.json()
    return Response({
        "quote": data[0]["q"],
        "author": data[0]["a"]
    })

