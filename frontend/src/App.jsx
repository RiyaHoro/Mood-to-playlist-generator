import React, { useState } from "react";
import "./index.css";
import MoodInput from "./MoodInput";
import Playlist from "./Playlist";

function App() {
  const [result, setResult] = useState(null);

  return (
    <div className="container">
      <h1 className="title">🎧 Mood-to-Playlist Generator</h1>
      <p className="subtitle">Type your mood or send emojis — we’ll match the vibe.</p>

      <MoodInput setResult={setResult} />

      {result && <Playlist result={result} />}
      
    </div>
  );
}

export default App;
