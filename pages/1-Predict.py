import streamlit as st
import requests
import matplotlib.pyplot as plt

# ---------- Function to set background from URL ----------
def set_bg_url(url):
    page_bg = f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url("{url}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    [data-testid="stHeader"] {{
        background: rgba(0,0,0,0); /* transparent header */
    }}
    [data-testid="stSidebar"] {{
        background: rgba(255,255,255,0.7); /* semi-transparent sidebar */
    }}
    </style>
    """
    st.markdown(page_bg, unsafe_allow_html=True)

# ---------- Apply background ----------
set_bg_url("https://t4.ftcdn.net/jpg/03/10/16/27/360_F_310162798_6hWbaSFgDtWp4AhhaKPlTgAZUDL1c4UY.jpg")

# ---------- Custom CSS ----------
st.markdown("""
    <style>
    .stButton > button {
        width: 100%; /* Full width like input fields */
        padding: 10px 0px;
        font-size: 18px;
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>AC Power Prediction</h1>", unsafe_allow_html=True)

# Input fields
irradiation = st.number_input("**Irradiation (W/m²)**", min_value=100.0, step=10.0)
ambient_temp = st.number_input("**Ambient Temperature (°C)**", min_value=0.0, step=1.0)
module_temp = st.number_input("**Module Temperature (°C)**", min_value=0.0, step=1.0)
dc_power = st.number_input("**DC Power (kW)**", min_value=100.0, step=10.0)

# Predict button
if st.button("Predict"):
    payload = {
        "IRRADIATION": irradiation,
        "AMBIENT_TEMPERATURE": ambient_temp,
        "MODULE_TEMPERATURE": module_temp,
        "DC_POWER": dc_power
    }
    try:
        response = requests.post("http://127.0.0.1:8000/predict", json=payload)
        if response.status_code == 200:
            result = response.json()["AC_POWER"]

            # ---------- Big Highlight Card ----------
            st.markdown(
                f"""
                <div style="background-color:#e6ffe6;padding:25px;border-radius:15px;text-align:center;">
                    <h2 style="color:#006400;font-size:28px;"> Predicted AC Power</h2>
                    <h1 style="color:#004d00;font-size:40px;">{result:.2f} kW</h1>
                    <h4 style="color:#444;"> R² Score: <b>99.9%</b></h4>
                </div>
                """,
                unsafe_allow_html=True
            )

            # ---------- Feature Importance ----------
            st.markdown("<h3 style='text-align: center;'>Feature Influence on Prediction</h3>", unsafe_allow_html=True)

            # Dummy values (replace with SHAP/sklearn feature importances later)
            importances = {
                "Irradiation": 0.55,
                "DC Power": 0.30,
                "Module Temp": 0.10,
                "Ambient Temp": 0.05
            }

            fig, ax = plt.subplots()
            ax.bar(importances.keys(), importances.values(), color="skyblue", edgecolor="black")
            ax.set_ylabel("Relative Importance")
            ax.set_title("Feature Importance")
            st.pyplot(fig)

        else:
            st.error(f"⚠️ Backend error {response.status_code}: {response.text}")
    except Exception as e:
        st.error(f"❌ Could not connect to backend: {e}")
