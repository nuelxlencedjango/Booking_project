import React from "react";
import BookingTable from "./Components/BookingTables";
import Booking from "./Components/BookingForm";
import FlatCreation from "./Components/FlatForm";



function App() {
  return (
    <div className="app-container"> <h3>Welcome to our booking platform</h3>
    <div className="App">
      <div className="sub-app-content">
        <BookingTable />
      </div>
      <div className="sub-app-content">
        <FlatCreation />
      </div>
      <div className="sub-app-content">
        <Booking />
      </div>
      
    </div>
    </div>
  );
}

export default App;
