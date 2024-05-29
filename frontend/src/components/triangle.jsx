import React, { useState } from 'react';
import './triangle.css'; 

function Triangle() {
  const [triangle, setTriangle] = useState([]);

  const generateRandomValue = () => {
    return Math.floor(Math.random() * 100);
  };

  const generateRandomTriangle = () => {
    const rows = [];

    for (let i = 1; i <= 100; i++) {
      const inputs = [];
      for (let j = 0; j < i; j++) {
        inputs.push(<input key={j} value={generateRandomValue()} />);
      }
      rows.push(inputs);
    }
    console.log({ rows })
    setTriangle(rows);
  };

  return (
    <div>
      <div>
        {triangle.map((row, index) => (
          <div key={index} className="row">{row}</div>
        ))}
      </div>
      <button onClick={generateRandomTriangle}>Llenar Aleatoriamente</button>
    </div>
  );
}

export default Triangle;
