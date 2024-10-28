import streamlit as st
import webbrowser
from time import sleep
# Set page title
st.title("Stock Price Prediction with ARIMA")

# Create two large buttons side-by-side
col1, col2 = st.columns(2)

# Button for Vietnam link
with col1:
    if st.button("Vietnam", use_container_width=True):
        st.write("Redirecting to Vietnam ARIMA prediction...")
        sleep(0.5)
        webbrowser.open_new_tab('https://arimavn.streamlit.app/')

# Button for World link
with col2:
    if st.button("Global", use_container_width=True):
        st.write("Redirecting to Global ARIMA prediction...")
        webbrowser.open_new_tab('https://arimavn.streamlit.app/')
        sleep(0.5)
