// import

// actions

// action creators

// initial state

const initialState = {
    isLoggoedIn: localStorage.getItem("jwt") || false,
};

// reducer
function reducer(state = initialState, action) {
    switch(action.type) {
        default:        return state;
    }
}

// reducer function

// exports

// reducer dexport
export default reducer;