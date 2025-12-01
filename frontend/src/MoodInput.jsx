import React, { useState } from "react";
import { predictMood } from "./api";
import "./input.css";

function MoodInput({ setResult }) {
  const [text, setText] = useState("");
  const [loading, setLoading] = useState(false);

  const sendMood = async () => {
    if (!text.trim()) return;
    setLoading(true);

    const data = await predictMood(text);
    setResult(data);
    setLoading(false);
  };

  return (
    <div className="input-container">
      <textarea
        className="mood-input"
        placeholder="Type your mood... 😔✨"
        value={text}
        onChange={(e) => setText(e.target.value)}
        rows="3"
      />

      <button className="generate-btn" onClick={sendMood}>
        {loading ? "Analyzing..." : "Get Playlist 🎧"}
      </button>
    </div>
  );
}

export default MoodInput;
