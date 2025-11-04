import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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
set_bg_url("https://framerusercontent.com/images/WJVdfRym2SQQEg4IRA1pp2lfqTI.jpg")

# ---------- Page Config ----------
st.set_page_config(page_title="Data Analysis", layout="wide")

# ---------- Title ----------
st.markdown("<h1 style='text-align: center;'>📊 Solar Plant Data Analysis</h1>", unsafe_allow_html=True)

# ---------- Custom CSS ----------
st.markdown("""
    <style>
    .uploadedFileLabel {
        font-size: 1.5rem !important; /* same as st.subheader */
        font-weight: 600 !important;
        color: black !important;
        text-align: center;
        display: block;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- File uploader ----------
st.markdown('<p class="uploadedFileLabel">📂 Upload Solar Plant CSV</p>', unsafe_allow_html=True)
uploaded_file = st.file_uploader("", type=["csv"])

# ---------- Data Analysis ----------
if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.write("###  Preview of Data")
    st.dataframe(df.head())

    # ---- Correlation Heatmap ----
    st.subheader("🔗 Correlation Heatmap")
    try:
        numeric_df = df.select_dtypes(include=['float64', 'int64'])
        numeric_df = numeric_df.drop(columns=['PLANT_ID'], errors='ignore')

        corr = numeric_df.corr()

        fig, ax = plt.subplots(figsize=(8, 6))
        sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax, fmt=".2f")
        st.pyplot(fig)

    except Exception as e:
        st.error(f"⚠️ Error while generating heatmap: {e}")

    # ---- Key Insight ----
    st.info("""
     **Irradiation** plays the most crucial role in solar power generation.  
    It directly drives the DC power produced by the panels, which is then 
    converted into AC power. This makes its relationship with AC power the 
    strongest among all factors.
    """)
    
    # ---- Scatter Plot ----
    st.subheader("📈 Irradiation vs AC Power")
    if "IRRADIATION" in df.columns and "AC_POWER" in df.columns:
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.scatterplot(x="IRRADIATION", y="AC_POWER", data=df, ax=ax, alpha=0.6)
        ax.set_title("Irradiation vs AC Power")
        st.pyplot(fig)
    else:
        st.warning("⚠️ Columns 'IRRADIATION' or 'AC_POWER' not found in dataset")