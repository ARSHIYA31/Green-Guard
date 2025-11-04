import streamlit as st

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
    .content {{
        text-align: center;
        color: black;
        max-width: 900px;
        margin: auto;
    }}
    </style>
    """
    st.markdown(page_bg, unsafe_allow_html=True)

# ---------- Apply background ----------
set_bg_url("https://t4.ftcdn.net/jpg/06/27/85/69/360_F_627856931_jXu5tya5vYOd3rlP6ObYNOvxyp6xtVLY.jpg")

# ---------- Page Config ----------
st.set_page_config(page_title="GreenGuard App", layout="wide")

# ---------- Main Content ----------
st.markdown(
    """
    <div class="content">
        <h1> GreenGuard: Solar Power Prediction & Monitoring</h1>
        <p style="font-size:18px;">
            Welcome to <b>GreenGuard</b>, a smart solar plant performance prediction tool powered by <b>Machine Learning</b>.  
            It predicts <b>AC Power output</b> using key features like 
            <b>Irradiation</b>, <b>Ambient Temperature</b>, <b>Module Temperature</b>, and <b>DC Power</b>.
        </p>
        <p style="font-size:18px;">
            With an impressive <b>R² ≈ 0.99</b>, the model can explain almost all variations in AC power, making it a powerful tool for 
            <b>forecasting plant performance</b>, <b>optimizing efficiency</b>, and <b>smarter energy management</b>.
        </p>
        <h3>Navigate through the sidebar to:</h3>
        <ul style="list-style-type:none; font-size:16px; line-height:1.8;">
            <li>🔮 <b>Predict</b> AC Power generation</li>
            <li>📊 <b>Analyze</b> plant & weather data</li>
            <li>🧠 <b>Explore</b> model details and performance</li>
            <li>ℹ️ <b>About</b> the project</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True
)
