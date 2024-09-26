from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Booking,Flat
from .serializers import BookingSerializer,FlatSerializer,BookingCreationSerializer






# Flat creation view
class FlatListCreate(generics.ListCreateAPIView):
    queryset = Flat.objects.all()
    serializer_class = FlatSerializer




# Booking view with previous booking ID logic
class BookingListCreate(generics.ListCreateAPIView):
    queryset = Booking.objects.all().select_related('flat').order_by('flat_id', 'checkin')
    serializer_class = BookingCreationSerializer





class BookingListView(APIView):
    def get(self, request):
        # Get sort and filtering using checkin object
        sort_by_checkin = request.GET.get('sort_by_checkin', False)
        #all objects in Booking
        bookings = Booking.objects.all()

        # 'only checkin
        if sort_by_checkin:
            bookings = bookings.order_by('checkin')

        #sorting by flat name 
        flat_name = request.GET.get('flat_name')
        if flat_name:
            bookings = bookings.filter(flat__name__icontains=flat_name)

        #return the filtered
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)
