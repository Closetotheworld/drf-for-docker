from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Routine
from .serializers import RoutineSerializer

# Create your views here.

@api_view(['GET'])
def helloAPI(request):
    return Response(200)

@api_view(['GET'])
def showRoutine(request):
    totalRoutine = Routine.objects.all()
    serializer = RoutineSerializer(totalRoutine, many=True)
    return Response(serializer.data)