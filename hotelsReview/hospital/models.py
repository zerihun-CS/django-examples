from django.db import models
from datetime import date, timedelta
# Create your models here.


GENDER = (
    ("MALE", "MALE"),
    ("FEMALE", "FEMALE"),
)

class Patient(models.Model):
   full_name = models.CharField(max_length=100,)
   address = models.CharField(max_length=100)
   phone = models.CharField(max_length=11,blank=True)
   date_of_birth = models.DateField()
   gender = models.CharField(max_length=11, choices = GENDER,)
   
   def age(self):
      age = (date.today() - self.date_of_birth) // timedelta(days=365.2425)
      return age

class Specializations(models.Model):
   name = models.CharField(max_length=50)

   def __str__(self) -> str:
      return self.name
   
   
class Doctor(models.Model):
   full_name = models.CharField(max_length=100,)
   address = models.CharField(max_length=100)
   phone = models.CharField(max_length=11,blank=True)
   position  = models.CharField(max_length=11)
   specialization  = models.ForeignKey("Specializations", on_delete=models.CASCADE)
   active = models.BooleanField(default=True)
   

class PatientHistory(models.Model):
   patient = models.ForeignKey("Patient", on_delete=models.CASCADE)
   doctor = models.ForeignKey(Doctor,on_delete=models.SET_NULL, null=True)
   date = models.DateTimeField(auto_now_add=True, null=True)
   diagnoses  = models.TextField()
   
   