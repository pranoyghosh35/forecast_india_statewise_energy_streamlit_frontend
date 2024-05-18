# State wise Annual Energy Forecast for India

# Try now: https://forecast-india-statewise-energy.onrender.com

This repository holds a Streamlit app (<b>frontend</b>) for the backend service that forecasts India's energy requirement and generation for any state, any year. Also find command used to build Docker image and deploy as a web service on render.

The backend is live at URI='https://forecast-india-statewise-energy-backend.onrender.com/predict'.
Hit it from anywhere with json containing 3 fields, e.g.:

```json
{
"State/Union Territory": "West Bengal",
"End_Year": 2024,
"population(crores)": 9.97
}
```

output:
```json
{
    "avail_crore_kWh": 6720.77,
    "req_crore_kWh": 7481.98
}
```

# The backend repository is at: 
https://github.com/pranoyghosh35/forecast_india_statewise_energy_backend.git

# Feel free to distribute,include and reuse but give credits!!
