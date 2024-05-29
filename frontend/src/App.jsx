import Triangle from './components/triangle'
import './App.css'
import { useState } from 'react'

function App() {
  const [value, setValue] = useState(0)


  return (
    <main>
      <div>
        <h1>
          PROGRAMACIÓN DINÁMICA
        </h1>
      </div>
      <Triangle />
      <button onClick={value => setValue(Math.floor(Math.random() * 10000)+100)}>
        calcular
      </button>
      <div>
        <p>{value}</p>
      </div>
    </main>
  )
}

export default App
