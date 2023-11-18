import React, { useState } from 'react';

const RadioButton = ({mode , modeSetter}) => {
  const [selectedValue, setSelectedValue] = useState('medium');

  const handleRadioChange = (event) => {
    setSelectedValue(event.target.value);
    modeSetter(event.target.value)
  };

  return (
    <div>
      {mode?<h3>{mode}</h3>:<></>}
      <label>
        <input
          type="radio"
          value="high"
          checked={selectedValue === 'high'}
          onChange={handleRadioChange}
        />
        High
      </label>

      <label>
        <input
          type="radio"
          value="medium"
          checked={selectedValue === 'medium'}
          onChange={handleRadioChange}
        />
        Medium
      </label>

      <label>
        <input
          type="radio"
          value="low"
          checked={selectedValue === 'low'}
          onChange={handleRadioChange}
        />
        Low
      </label>

    </div>
  );
};

export default RadioButton;
