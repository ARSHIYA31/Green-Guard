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
    </style>
    """
    st.markdown(page_bg, unsafe_allow_html=True)

# ---------- Apply background ----------
set_bg_url("https://thumb.ac-illust.com/75/75c8741dddf63d5030ea0b8064f64cc3_t.jpeg")  # replace with your own URL



st.title("🔰 About GreenGuard")

st.markdown("""
GreenGuard is a **solar power monitoring and prediction tool** built with:  
- 🐍 Python (Pandas, Scikit-learn)  
- ⚡ Machine Learning (Random Forest Regressor)  
- 🌐 FastAPI (Backend API)  
- 🎨 Streamlit (Frontend Dashboard)  

### 🎯Aim :
- Predict **AC Power output** from weather + plant parameters  
- Visualize **solar performance & trends**  
- Provide insights into **plant efficiency**  
""")

st.title("🧠 Model Information")

st.markdown("""
This **Random Forest Regression model** was trained on solar plant data with features:  

- ☀️ Irradiation  
- 🌡️ Ambient Temperature  
- 🔥 Module Temperature  
- ⚡ DC Power  

### 🦾 Performance Metrics:
- **MAE:** 0.12  
- **RMSE:** 0.65  
- **R² Score:** 0.99  
            
""")
