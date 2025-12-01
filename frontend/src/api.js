import axios from "axios";

const API = "https://mood-to-playlist-generator.onrender.com";

export const predictMood = async (text) => {
  const res = await axios.post(`${API}/predict`, { text });
  return res.data;
};
