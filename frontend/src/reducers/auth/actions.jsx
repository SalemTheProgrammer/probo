// actions.js
import axios from 'axios';
import {
  REGISTER_SUCCESS,
  REGISTER_FAIL,
  LOGIN_SUCCESS,
  LOGIN_FAIL,
  LOGOUT,
  AUTH_LOADING,
  AUTH_ERROR,
  RESET_PASSWORD_SUCCESS,
  RESET_PASSWORD_FAIL,
  REFRESH_TOKEN,
} from './actions';

const BASE_URL = import.meta.env.VITE_BASE_URL;

export const register = (username, email, password) => async (dispatch) => {
  dispatch({ type: AUTH_LOADING });
  try {
    const response = await axios.post(`${BASE_URL}/register`, { username, email, password });
    dispatch({ type: REGISTER_SUCCESS, payload: response.data });
  } catch (error) {
    dispatch({ type: REGISTER_FAIL, payload: error.response ? error.response.data : error.message });
  }
};

export const login = (email, password) => async (dispatch) => {
  dispatch({ type: AUTH_LOADING });
  try {
    const response = await axios.post(`${BASE_URL}/login`, { email, password });
    dispatch({ type: LOGIN_SUCCESS, payload: response.data });
  } catch (error) {
    dispatch({ type: LOGIN_FAIL, payload: error.response ? error.response.data : error.message });
  }
};

export const logout = () => async (dispatch) => {
  // Add any necessary logout logic here, such as calling an API endpoint
  dispatch({ type: LOGOUT });
};

export const resetPassword = (email) => async (dispatch) => {
  dispatch({ type: AUTH_LOADING });
  try {
    const response = await axios.post(`${BASE_URL}/reset_password`, { email });
    dispatch({ type: RESET_PASSWORD_SUCCESS, payload: response.data });
  } catch (error) {
    dispatch({ type: RESET_PASSWORD_FAIL, payload: error.response ? error.response.data : error.message });
  }
};

export const refreshToken = () => async (dispatch) => {
  dispatch({ type: AUTH_LOADING });
  try {
    const response = await axios.post(`${BASE_URL}/refresh`);
    dispatch({ type: REFRESH_TOKEN, payload: response.data });
  } catch (error) {
    dispatch({ type: AUTH_ERROR, payload: error.response ? error.response.data : error.message });
  }
};
