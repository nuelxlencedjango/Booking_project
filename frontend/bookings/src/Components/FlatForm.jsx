import React, { useState } from 'react';
import axios from 'axios';


const FlatForm = () => {
  const [name, setName] = useState('');
  const [successMessage, setSuccessMessage] = useState('');
  const [errorMessage, setErrorMessage] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setSuccessMessage('');
    setErrorMessage('');

    try {
      await axios.post('http://127.0.0.1:8000/api/create-flats/', { name });
      alert('Flat created successfully');
      setSuccessMessage('Flat created successfully');
      setName(''); 
    } catch (error) {
      if (error.response && error.response.data) {
        const errors = error.response.data;
        if (errors.name) {
          setErrorMessage(errors.name.join(' '));
        } else {
          setErrorMessage('An error occurred. Please try again.');
        }
      } else {
        setErrorMessage('There was an error creating the flat.');
      }
    }
  };

  return (
    <div className="form-container">
      <h2>Add a Flat</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={name}
          onChange={(e) => setName(e.target.value)}
          placeholder="Flat Name"
          required
        />

      
        {errorMessage && <div className="error-message">{errorMessage}</div>}

     
        {successMessage && <div className="success-message">{successMessage}</div>}

        <button type="submit">Add Flat</button>
      </form>
    </div>
  );
};

export default FlatForm;
