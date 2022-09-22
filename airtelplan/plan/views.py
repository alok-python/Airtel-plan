from webbrowser import get
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import AirtelPlan
from .serializer import AirtelSerializer

from rest_framework import viewsets

# Create your views here.


def airtel(request):
    plan=AirtelPlan.objects.all()
    content={'plan':plan}
    return render(request,'index.html',content)

class Airtel_plan(viewsets.ModelViewSet):
    queryset= AirtelPlan.objects.all()
    serializer_class=AirtelSerializer