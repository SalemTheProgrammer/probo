import { combineReducers } from 'redux';
import authReducer from './auth/authReducer';

const initialState = {
  counter: 0,
};

const counterReducer = (state = initialState, action) => {
  switch (action.type) {
    case 'INCREMENT':
      return { ...state, counter: state.counter + 1 };
    case 'DECREMENT':
      return { ...state, counter: state.counter - 1 };
    default:
      return state;
  }
};

const rootReducer = combineReducers({
  counter: counterReducer,
  auth : authReducer
});

export default rootReducer;