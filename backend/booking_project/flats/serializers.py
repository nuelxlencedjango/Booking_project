

from rest_framework import serializers
from .models import Flat, Booking
import datetime
class FlatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flat
        fields = ['id', 'name']




#serializer for creating booking objects
class BookingCreationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = ['id',  'flat', 'checkin', 'checkout']

    

#serializer for retriving/reading booking objects
class BookingSerializer(serializers.ModelSerializer):
    previous_booking_id = serializers.SerializerMethodField()
    flat_name = serializers.CharField(source='flat.name', read_only=True)
    checkin = serializers.DateField(format='%Y-%m-%d')
    checkout = serializers.DateField(format="%Y-%m-%d")
   
    class Meta:
        model = Booking
        fields = ['id',  'flat_name', 'checkin', 'checkout', 'previous_booking_id']
     
    # check if previous booking exist,else return -
    def get_previous_booking_id(self, obj):
        previous_booking = obj.get_previous_booking()
        return previous_booking.id if previous_booking else '-'

    


    
