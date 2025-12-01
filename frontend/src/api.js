import axios from "axios";

const API = "http://127.0.0.1:8000";

export const predictMood = async (text) => {
  const res = await axios.post(`${API}/predict`, { text });
  return res.data;
};
