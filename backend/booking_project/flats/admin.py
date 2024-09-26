from django.contrib import admin
from .models import  Booking,Flat
# Register your models here.




class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'flat', 'checkin','checkout')
    list_filter = ("flat", 'checkin')
    search_fields = ['id', 'checkin']
    #prepopulated_fields = {'id': ('checkout',)}

admin.site.register(Booking, BookingAdmin)

admin.site.register(Flat)

