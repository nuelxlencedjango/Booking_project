
import React, { useState, useEffect } from 'react';
import axios from 'axios';


const BookingForm = () => {
  const [flats, setFlats] = useState([]);
  const [flatId, setFlatId] = useState('');
  const [checkin, setCheckin] = useState('');
  const [checkout, setCheckout] = useState('');
  const [successMessage, setSuccessMessage] = useState('');
  const [errorMessage, setErrorMessage] = useState('');


  useEffect(() => {
    const fetchFlats = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/create-flats/');
        setFlats(response.data);
      } catch (error) {
        console.error('There was an error fetching the flats!', error);
      }
    };
    fetchFlats();
  }, []);

  // Handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault();
    setSuccessMessage('');
    setErrorMessage('');

    // Validate checkin and checkout dates
    if (new Date(checkin) >= new Date(checkout)) {
      setErrorMessage('Check-out date must be after the check-in date.');
      return;
    }

    // Create booking
    try {
      await axios.post('http://127.0.0.1:8000/api/booking-creation/', {
        flat: flatId,
        checkin,
        checkout,
      });
      alert('Booking created successfully!')
      setSuccessMessage('Booking created successfully!');
      setFlatId(''); 
      setCheckin('');
      setCheckout('');
    } catch (error) {
      setErrorMessage('There was an error creating the booking. Please try again.');
      console.error('Error creating booking:', error);
    }
  };

  return (
    <div className="form-container">
      <h2>Create a Booking</h2>

      <form onSubmit={handleSubmit}>
    
        <label htmlFor="flat">Select Flat:</label>
        <select
          id="flat"
          value={flatId}
          onChange={(e) => setFlatId(e.target.value)}
          required
        >
          <option value="">Select a flat</option>
          {flats.map((flat) => (
            <option key={flat.id} value={flat.id}>
              {flat.name}
            </option>
          ))}
        </select>

        {/* Check-in date */}
        <label htmlFor="checkin">Check-in Date:</label>
        <input
          type="date"
          id="checkin"
          value={checkin}
          onChange={(e) => setCheckin(e.target.value)}
          required
        />

        {/* Check-out date */}
        <label htmlFor="checkout">Check-out Date:</label>
        <input
          type="date"
          id="checkout"
          value={checkout}
          onChange={(e) => setCheckout(e.target.value)}
          required
        />

   
        {errorMessage && <div className="error-message">{errorMessage}</div>}

    
        {successMessage && <div className="success-message">{successMessage}</div>}

        <button type="submit">Add Booking</button>
      </form>
    </div>
  );
};

export default BookingForm;
