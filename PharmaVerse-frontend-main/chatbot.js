import React, { useState } from "react";

const Chatbot = () => {
  const [message, setMessage] = useState("");
  const [response, setResponse] = useState("");

  const sendMessage = async () => {
    const res = await fetch("http://localhost:5000/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message }),
    });
    const data = await res.json();
    setResponse(data.response);
  };

  return (
    <div className="chat-container">
      <h2>PharmaVerse AI Chatbot</h2>
      <input 
        type="text" 
        value={message} 
        onChange={(e) => setMessage(e.target.value)} 
        placeholder="Ask PharmaVerse AI..." 
      />
      <button onClick={sendMessage}>Send</button>
      <p><strong>Response:</strong> {response}</p>
    </div>
  );
};

export default Chatbot;
