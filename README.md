# Try now: https://forecast-india-statewise-energy.onrender.com

This repository holds a Streamlit app for the backend service that forecasts India's energy requirement and generation for any state, any year.Also command to build Docker image and deploy web service on render.

The backend is live at URI='https://forecast-india-statewise-energy-backend.onrender.com/predict'.
Hit it with json containing 3 fields, e.g.:

{
"State/Union Territory": "West Bengal",
"End_Year": 2024,
"population(crores)": 9.97
}

output:

{
    "avail_crore_kWh": 6720.77,
    "req_crore_kWh": 7481.98
}
