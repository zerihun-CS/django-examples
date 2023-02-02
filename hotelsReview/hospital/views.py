from django.shortcuts import render, get_object_or_404
from .models import Doctor, Patient,PatientHistory,Specializations
# Create your views here.


def doctor_view(request):   
   data = {
      'doctor':Doctor.objects.all()
   }
   return render(request, "home.html",data)

def patient_view(request):
   data = {
      'patient':Patient.objects.all()
   }
   return render(request,'patient.html',data)

def  patient_history(request, patient_id ):
   history = PatientHistory.objects.filter(patient = patient_id)
   
   data = {
      'history':history
   }
   return render(request, 'patient_history.html', data)
   
   
def doctor_crud(request):
   sp = Specializations.objects.all()
   if request.method == 'POST':
      name = request.POST.get('name')
      address = request.POST.get('address')
      position = request.POST.get('postion')
      specialization = request.POST.get('specialization')
      
      specialization_obj1 = Specializations.objects.filter(id = specialization).first()
      
      
      
      obj1 = Doctor()
      
      obj1.full_name = name
      obj1.address = address
      obj1.position = position
      obj1.specialization = specialization_obj1
      obj1.save()
   
   return render(request, 'doctor_crud.html',{'sp':sp} )