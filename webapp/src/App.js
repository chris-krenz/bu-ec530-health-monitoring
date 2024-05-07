import logo from './logo.svg';
import './App.css';
import React, { useEffect, useState } from 'react'
import Button from '@mui/material/Button';
import Box, { BoxProps } from '@mui/material/Box';
import axios from 'axios';

const url = "http://localhost:8000/api";

function App() {

  const [data, setData] = useState(null);
  const [uid1, setUID1] = useState(null);
  const [uid2, setUID2] = useState(null);
  const [name, setName] = useState(null);
  const [ssn, setSSN] = useState(null);
  const [email, setEmail] = useState(null);
  const [role, setRole] = useState(null);

  const get = () => {
    fetch(url.concat('/', 'users/', uid1), {
      method: 'GET'
    })
      .then(response => response.json())
      .then(json => setData(json))
      .catch(error => console.error(error));
  }

  const put = () => {
    fetch(url.concat('/', 'users/', uid2), {
      method: 'PUT',
      headers: new Headers({ 'Content-Type': 'application/json' }),
      body: JSON.stringify({ 'uid': uid2, 'name': name, 'ssn': ssn, 'email': email, 'role': role })
    })
      .then(response => response.json())
      .then(json => setData(json))
      .catch(error => console.error(error));
  }

  const del = () => {
    fetch(url.concat('/', 'users/', uid1), {
      method: 'DELETE'
    })
      .then(response => response.json())
      .then(json => setData(json))
      .catch(error => console.error(error));
  }

  // Alternative using Fetch
  // useEffect(() => {
  //   fetch(url.concat('/', 'users/pull/', uid))
  //     .then(response => response.json())
  //     .then(json => setData(json))
  //     .catch(error => console.error(error));
  // }, [crud]);

  // Alternative: use Axios
  // useEffect(() => {
  //   axios.get(url.concat('/', 'users/', uid))  // 'data' to test
  //     .then(response => {
  //       setData(response.data);
  //     })
  //     .catch(error => {
  //       console.error(error);
  //     });
  // }, [input]);

  return (
    <div className="App">
      <header className="App-header">
        <Box sx={{ display: 'flex-start', flexDirection: 'row', textAlign: 'left', textAlign: "top" }}>
          <p>
            Health System Records App<br />
          </p>
          <span style={{ fontSize: 20 }}>UID: &nbsp;</span>
          <input name="uid1" onChange={e => { console.log(e.target.value); setUID1(e.target.value); }} />
          <Button onClick={() => { get() }} variant="contained" sx={{ ml: 3 }}>
            Retrieve Record
          </Button>
          <Button onClick={() => { del() }} color="error" variant="contained" sx={{ ml: 3 }}>
            Delete Record
          </Button>
          <div style={{ textAlign: "left", fontSize: 18 }}>
            {data ? <pre>{JSON.stringify(data, null, 2).
              replaceAll("{", "").
              replaceAll("}", "").
              replaceAll('"', "").
              replaceAll(',', "")}</pre> : '...'}
          </div>
        </Box>
        <Box sx={{ display: 'flex', flexDirection: 'column', textAlign: 'left', width: 180 }} >
          <div style={{ fontSize: 20, margin: 10 }}>
            UID: <input name="uid2" onChange={e => { console.log(e.target.value); setUID2(e.target.value); }} />
          </div>
          <div style={{ fontSize: 20, margin: 10 }}>
            Name: <input name="name" onChange={e => { console.log(e.target.value); setName(e.target.value); }} />
          </div>
          <div style={{ fontSize: 20, margin: 10 }}>
            SSN: <input name="ssn" onChange={e => { console.log(e.target.value); setSSN(e.target.value); }} />
          </div>
          <div style={{ fontSize: 20, margin: 10 }}>
            Email: <input name="email" onChange={e => { console.log(e.target.value); setEmail(e.target.value); }} />
          </div>
          <div style={{ fontSize: 20, margin: 10 }}>
            Role: <input name="role" onChange={e => { console.log(e.target.value); setRole(e.target.value); }} />
          </div>
        </Box>
        <Button onClick={() => { put() }} color="success" variant="contained" sx={{ m: 5, textAlign: 'left', width: 200 }}>
          Create Record
        </Button>
      </header>
    </div>
  );
}

export default App;
