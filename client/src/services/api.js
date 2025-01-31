import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'https://micro-donation-platform.onrender.com/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export default api;
