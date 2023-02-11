from django.db import models

class ROOMS(models.Model):
    room_id= models.CharField(max_length=255)
    maximum_room_occupancy= models.IntegerField()
    guest_email= models.CharField(max_length=255)
    room_status= models.CharField(max_length=255)
    
    class Meta:
        db_table="room_information"
