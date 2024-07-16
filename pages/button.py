import streamlit as st
if 'key' not in st.session_state:
    st.session_state.key = "null"

st.button("Reset", type='primary')
if st.button("say hello"):
    st.session_state.key = "Hi"
else :
    st.session_state.key = "Bye"