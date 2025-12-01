import React, { useState } from "react";
import { predictMood } from "./api";

function MoodInput({ setResult }) {
  const [text, setText] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSend = async () => {
    if (!text.trim()) return;
    setLoading(true);

    const data = await predictMood(text);
    setResult(data);

    setLoading(false);
  };

  return (
    <div className="input-section">
      <textarea
        className="input-box"
        placeholder="Describe your mood… 😔✨"
        value={text}
        onChange={(e) => setText(e.target.value)}
        rows="3"
      />

      <button className="btn" onClick={handleSend} disabled={loading}>
        {loading ? "Generating..." : "Generate Playlist 🎵"}
      </button>
    </div>
  );
}

export default MoodInput;
