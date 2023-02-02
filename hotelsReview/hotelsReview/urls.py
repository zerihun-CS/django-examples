"""hotelsReview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hospital.views import doctor_view,patient_view,patient_history,doctor_crud
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',doctor_view, name="home_url"),
    path('patient/',patient_view,name="patient_url" ),
    path('patient/<int:patient_id>/',patient_history, name="patient_history_url")
    path('patient/<int:patient_id>/',doctor_crud, name="patient_history_url")
    
]
