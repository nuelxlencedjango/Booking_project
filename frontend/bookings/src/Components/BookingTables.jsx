import React, { useEffect, useState } from "react";
import axios from "axios";

function BookingTable() {
    // handling booking,sortorder and errors
    const [bookings, setBookings] = useState([]);
    const [sortOrder, setSortOrder] = useState('checkin');
    const [error, setError] = useState('');

    //calling fetchbooking functions and sorting 
    useEffect(() => {
        fetchBookings();
    }, [sortOrder]);

    const fetchBookings = () => {
        // Reset error before fetching
        setError(''); 
        const query = sortOrder === 'checkin' ? '?sort_by_checkin=true' : '';
        //Api call to booking  
        axios
            .get(`http://localhost:8000/${query}`)
            .then(response => setBookings(response.data))
            .catch(error => {
                console.error('Error fetching bookings:', error);
                setError('Failed to fetch bookings. Please try again later.');
            });
    };

    const handleSortChange = (event) => {
        setSortOrder(event.target.value);
    };


    return (
        <div className="book-platform">
            <div className="table-content">
                <div>
                    <h2>Sort by ID or Checkin</h2>
                <select value={sortOrder} onChange={handleSortChange}>
                    <option value="checkin">Checkin</option>
                    <option value="id">ID</option>
                </select>
                </div>

                {error && <p className="error-message">{error}</p>}

                {!error && bookings.length > 0 ? (
                    <table>
                        <thead>
                            <tr>
                                <th>Flat Name</th>
                                <th>ID</th>
                                <th>Checkin</th>
                                <th>Checkout</th>
                                <th>Previous Booking ID</th>
                            </tr>
                        </thead>
                        <tbody>
                            {bookings.map((booking) => (
                                <tr key={booking.id}>
                                    <td>{booking.flat_name}</td>
                                    <td>{booking.id}</td>
                                   
                                    <td>{booking.checkin}</td>
                                    <td>{booking.checkout}</td>
                                    <td>{booking.previous_booking_id || 'N/A'}</td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                ) : (
                    !error && <p>No bookings available.</p>
                )}
            </div>
        </div>
    );
}

export default BookingTable;
