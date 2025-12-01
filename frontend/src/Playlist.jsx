import React from "react";
import "./playlist.css";

function Playlist({ result }) {
  return (
    <div className="playlist-container">
      <h2 className="playlist-title">
        Mood Detected: <span className="mood">{result.mood} 🎧</span>
      </h2>

      <div className="playlist-grid">
        {result.playlist.map((song, index) => (
          <div className="song-card" key={index}>
            
            {/* Album Cover */}
            {song.image && (
              <img src={song.image} alt="Album Cover" className="album-art" />
            )}

            <div className="song-info">
              <h3 className="song-title">{song.song}</h3>
              <p className="song-artist">{song.artist}</p>

              {/* Audio Preview */}
              {song.preview && (
                <audio controls className="audio-player">
                  <source src={song.preview} type="audio/mpeg" />
                </audio>
              )}

              <a
                className="spotify-btn"
                href={song.link}
                target="_blank"
                rel="noopener noreferrer"
              >
                🎵 Play on Spotify
              </a>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Playlist;
