from django.test import TestCase
from .models import Flat, Booking
from .serializers import BookingSerializer
from django.urls import reverse
from rest_framework.test import APIClient  



# flat Model testing
class FlatModelTest(TestCase):
    def setUp(self):
        self.flat = Flat.objects.create(name='flat-1')

    def test_flat_creation(self):
        self.assertEqual(self.flat.name, 'flat-1')


#Booking model test
class BookingModelTest(TestCase):
    def setUp(self):
        self.flat = Flat.objects.create(name='flat-1')
        self.booking1 = Booking.objects.create(id=1, flat=self.flat, checkin="2022-01-01", checkout="2022-01-13")
        self.booking2 = Booking.objects.create(id=2, flat=self.flat, checkin="2022-01-20", checkout="2022-02-10", previous_booking_id=1)
        self.booking3 = Booking.objects.create(id=3, flat=self.flat, checkin="2022-02-20", checkout="2022-03-10", previous_booking_id=2)

        # testoing objects of bookings
    def test_booking_creation(self):
        self.assertEqual(self.booking1.flat.name, 'flat-1')
        self.assertEqual(self.booking1.checkin, "2022-01-01")
        self.assertEqual(self.booking1.checkout, "2022-01-13")
        self.assertEqual(self.booking2.previous_booking_id, 1)
    
        #testing previous ids
    def test_booking_previous_booking_id(self):
        self.assertIsNone(self.booking1.previous_booking_id)
        self.assertEqual(self.booking2.previous_booking_id, 1)
        self.assertEqual(self.booking3.previous_booking_id, 2)




# serializers testing
class BookingSerializerTest(TestCase):
    def setUp(self):
        self.flat = Flat.objects.create(name='flat-1')
        self.booking = Booking.objects.create(id=1, flat=self.flat, checkin="2022-01-01", checkout="2022-01-13")

    def test_booking_serialization(self):
        serializer = BookingSerializer(self.booking)
        data = serializer.data
        self.assertEqual(data['flat_name'], 'flat-1')
        self.assertEqual(data['checkin'], "2022-01-01")
        self.assertEqual(data['checkout'], "2022-01-13")

    def test_invalid_data(self):
        data = {
            'flat': self.flat.id,
            'checkin': '',
            'checkout': '2022-01-13'
        }
        serializer = BookingSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(set(serializer.errors.keys()), set(['checkin']))




#booking views test
class BookingViewAPIViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()  
        self.flat1 = Flat.objects.create(name='flat-1')
        self.flat2 = Flat.objects.create(name='flat-2')
        self.booking1 = Booking.objects.create(id=1, flat=self.flat1, checkin="2022-01-01", checkout="2022-01-13")
        self.booking2 = Booking.objects.create(id=2, flat=self.flat1, checkin="2022-01-20", checkout="2022-02-10", previous_booking_id=1)
        self.booking3 = Booking.objects.create(id=3, flat=self.flat1, checkin="2022-02-20", checkout="2022-03-10", previous_booking_id=2)
        self.booking4 = Booking.objects.create(id=4, flat=self.flat2, checkin="2022-01-02", checkout="2022-01-20")
        self.booking5 = Booking.objects.create(id=5, flat=self.flat2, checkin="2022-01-20", checkout="2022-02-11", previous_booking_id=4)

        #reading all booking objects
    def test_get_all_bookings(self):
        response = self.client.get(reverse('booking-creation'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 5)


    def test_sort_by_checkin(self):
         # sorting by booking and using reverse
        response = self.client.get(reverse('bookings') + '?sort_by_checkin=true') 
        self.assertEqual(response.status_code, 200)
         # Sorted by using checkin
        self.assertEqual(response.data[0]['id'], 1) 

    def test_create_booking(self):
        data = {
            'flat': self.flat1.id,
            'checkin': '2022-04-01',
            'checkout': '2022-04-10'
        }
        response = self.client.post(reverse('booking-creation'), data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Booking.objects.count(), 6)

    def test_invalid_booking_data(self):
        data = {
            'flat': self.flat1.id,
            'checkin': '',
            'checkout': '2022-04-10'
        }
        response = self.client.post(reverse('booking-creation'), data, format='json')
        self.assertEqual(response.status_code, 400)
