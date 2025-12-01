import React from "react";

function Playlist({ result }) {
  return (
    <div className="playlist-box">
      <h2 className="mood-title">
        Mood detected: <span className="mood">{result.mood} 🎶</span>
      </h2>

      <div className="song-list">
        {result.playlist.map((song, index) => (
          <div className="song-card" key={index}>
            <h3 className="song-name">{song.song}</h3>
            <p className="artist-name">{song.artist}</p>
            <a
              className="play-btn"
              href={song.link}
              target="_blank"
              rel="noopener noreferrer"
            >
              ▶ Play
            </a>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Playlist;
