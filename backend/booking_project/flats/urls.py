from django.urls import path
from .views import BookingListView,FlatListCreate,BookingListCreate

# the 3 view classes urls
urlpatterns = [
    path('',BookingListView.as_view(), name='bookings'), 
    path('api/create-flats/', FlatListCreate.as_view(), name="create-flats"),
    path('api/booking-creation/', BookingListCreate.as_view(), name="booking-creation"),



]


