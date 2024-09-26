from django.db import models
import datetime


#Flat models and making it unique- no 2 flats are the same
class Flat(models.Model):
    name = models.CharField(max_length=255, unique=True,blank=False,null=False)

    def __str__(self):
        return self.name


#booking model
class Booking(models.Model):
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE, related_name='bookings')
    checkin = models.DateField()
    checkout = models.DateField()
    previous_booking = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='next_bookings')
   
   #previous booking id if exists
    def get_previous_booking(self):
        # filtering booking models using checking to see which comes first and arranging it decending order
        return Booking.objects.filter(flat=self.flat, checkin__lt=self.checkin).order_by('-checkin').first()

    def __str__(self):
        return f"{self.flat.name} - {self.checkin} to {self.checkout}"
        #return f'{self.checkin.strftime("%Y-%m-%d")} to {self.checkout.strftime("%Y-%m-%d")}'
            

