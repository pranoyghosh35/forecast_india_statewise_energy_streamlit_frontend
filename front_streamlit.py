import streamlit as st
import requests
import json

st.title("Predict India's Annual Power Requirement & Availability")
st.image("data/india_bg.jpeg",width=400)
# Define form fields
state_ut = st.selectbox(
    "State/Union Territory:",
    ["Andaman and Nicobar Islands", "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar",
     "Chandigarh", "Chhattisgarh", "Dadra and Nagar Haveli", "Daman and Diu", "Delhi", "Goa",
     "Gujarat", "Haryana", "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka",
     "Kerala", "Lakshadweep", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram",
     "Nagaland", "Odisha", "Puducherry", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana",
     "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"]
)
end_year = st.text_input("Year:")
population = st.text_input("Population (crores):")

# Submit button
if st.button("Predict"):
    if state_ut and end_year and population:
        try:
            data = {
                "State/Union Territory": state_ut,
                "End_Year": end_year,
                "population(crores)": population
            }
            #this URL to point to your deployed Flask API
            URI='https://forecast-india-statewise-energy-backend.onrender.com/predict'
            response = requests.post(URI, json=data)
            result = response.json()
            st.write(f"Predicted Annual Power Requirement: {result['req_crore_kWh']} crores kWh")
            st.write(f"Predicted Annual Power Availability: {result['avail_crore_kWh']} crores kWh")
        except Exception as e:
            st.error(f"Error: {str(e)}")
    else:
        st.error("Please fill all the fields")
