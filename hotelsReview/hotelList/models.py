from django.db import models

# Create your models here.

class Hotel(models.Model):
   hotel_name = models.CharField(max_length=100)
   hotel_location  = models.CharField(max_length=100)
   hotel_map_address = models.URLField()
   
   def __str__(self):
      return self.hotel_name

   
class Menu(models.Model):
   hotel = models.ForeignKey("Hotel",  on_delete=models.CASCADE)
   dish_name = models.CharField(max_length=100)
   dish_price = models.FloatField()
   dish_indegriants  = models.TextField()
   
class Hall(models.Model):
   hotel = models.ForeignKey("Hotel",  on_delete=models.CASCADE)
   hall_name = models.CharField(max_length=100)
   max_attendee = models.IntegerField()



class RoomTypes(models.Model):
   
   type_name = models.CharField(max_length=100)

   def __str__(self):
      return self.type_name

class BedRooms(models.Model):
   
   hotel = models.ForeignKey("Hotel",  on_delete=models.CASCADE)
   room_image  = models.ImageField()
   room_types = models.ForeignKey("RoomTypes",  on_delete=models.CASCADE)
   price = models.FloatField()
   
   
