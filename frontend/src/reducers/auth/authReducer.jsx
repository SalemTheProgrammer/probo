const initialState = {
    isAuthenticated: false,
    user: null,
    loading: true,
    error: null,
  };
  
  const authReducer = (state = initialState, action) => {
    switch (action.type) {
      case 'LOGIN_SUCCESS':
        return {
          ...state,
          isAuthenticated: true,
          user: action.payload.user,
          loading: false,
          error: null,
        };
      case 'LOGIN_FAIL':
        return {
          ...state,
          isAuthenticated: false,
          user: null,
          loading: false,
          error: action.payload.error,
        };
      case 'LOGOUT':
        return {
          ...state,
          isAuthenticated: false,
          user: null,
          loading: false,
          error: null,
        };
      case 'AUTH_LOADING':
        return {
          ...state,
          loading: true,
        };
      case 'AUTH_ERROR':
        return {
          ...state,
          error: action.payload.error,
          loading: false,
        };
      default:
        return state;
    }
  };
  
  export default authReducer;
  