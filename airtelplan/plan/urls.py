from django.contrib import admin
from django.urls import path,include
from plan.views import Airtel_plan, airtel
from rest_framework import routers


router= routers.DefaultRouter()
router.register(r'',Airtel_plan)


urlpatterns = [   
    path("", airtel, name="home") ,
    path('product/',include(router.urls)),
    
]
