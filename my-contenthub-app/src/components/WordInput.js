// src/components/WordInput.js
import React, { useState } from 'react';
import RadioButton from './RadioButton';
import { ToastContainer, toast } from 'react-toastify';
import { Feedback } from './Feedback';

const WordInput = () => {
  const [words, setWords] = useState('');
  const [fetchedData, setFetchedData] = useState([]);
  const [creativity , setCreativity] = useState('medium')
  const [tone , setTone] = useState('medium')
  const [style , setStyle] = useState('medium')

  const handleInputChange = (e) => {
    setWords(e.target.value);
  };


 
  const sendData = () => {

    console.log("my mode ", creativity , tone , style)
    
    fetch('http://127.0.0.1:5000/main/process-words', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },

      body: JSON.stringify({ words: words.split(' ') , modes : {creativity: creativity , style: style , tone : tone}}),
    })
      .then(response => response.json())
      .then(data => {
        console.log('Response from Flask:', data);
        setFetchedData(data.processed_words || []); // Assuming processed_words is the key from Flask
      })
      .catch(error => {
        console.error('Error:', error);
      });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    sendData();
  };

  const handleDivClick = (value) => {
    console.log('Clicked:', value); // Perform actions when a value is clicked
  };

  return (
    <div>
      
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Enter words separated by spaces"
          value={words}
          onChange={handleInputChange}
        />
        <RadioButton mode={"creativity"} modeSetter = {setCreativity}/>
        <RadioButton mode={"style"} modeSetter = {setStyle}/>
        <RadioButton mode={"tone"} modeSetter = {setTone}/>
        <button type="submit">Send Words</button>
      </form>
      <div>
        {fetchedData.map((item, index) => (
          
          <div key={index}>
            <div  onClick={() => handleDivClick(item)}>
              {item}
              
            </div>
            <Feedback slogan={item} keywords={words}/>
            
          </div>
          
        ))}
      </div>
    </div>
  );
};

export default WordInput;
