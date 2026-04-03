import React, { useState } from "react";
import axios from "axios";

function App() {
  const [token, setToken] = useState("");

  const login = async () => {
    const res = await axios.post("http://localhost:5001/login", {
      username: "admin",
      password: "password"
    });
    setToken(res.data.token);
  };

  const transfer = async () => {
    await axios.post("http://localhost:5002/transfer", {
      from: 1,
      to: 2,
      amount: 500
    }, {
      headers: { Authorization: `Bearer ${token}` }
    });
    alert("Transfer Complete");
  };

  return (
    <div>
      <h1>Punjab & Sind Bank Dashboard</h1>
      <button onClick={login}>Login</button>
      <button onClick={transfer}>Transfer Money</button>
    </div>
  );
}

export default App;
