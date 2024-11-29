import React, { useState } from "react";

function App() {
  const [imageURL, setimageURL] = useState("");
  const [response, setResponse] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await fetch("http://127.0.0.1:8000/post", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ imageURL }),
      });
      console.log("Response status:", res.status);
      console.log("Response headers:", res.headers);
      const data = await res.json();
      setResponse(data.response);
    } catch (error) {
      console.error("Error:", error);
      setResponse("An error occurred.");
    }
  };

  const handleUpload = (e) => {
    if (e.target.files) {
      const url = URL.createObjectURL(e.target.files[0]);
      setimageURL(url);
    }
  };

  return (
    <div className="App">
      <h1>Animal identifier</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="file"
          onChange={(e) => handleUpload(e)}
          placeholder="Ask your question..."
        />
        <button type="submit">Submit</button>
      </form>
      <div>
        <h2>Response:</h2>
        <p>{response}</p>
      </div>
    </div>
  );
}

export default App;
