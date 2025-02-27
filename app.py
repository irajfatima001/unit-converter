
import streamlit as st

# ✅ Page Configuration
st.set_page_config(page_title="Astro Unit Converter", layout="wide")

# ✅ Corrected CSS
st.markdown(
    """
    <style>
    /* Background Styling */
    .stApp {
        background: linear-gradient(45deg, rgb(209, 214, 214), rgb(14, 167, 146));
        font-family: sans-serif !important;
        
        max-width: 500px; 
        padding: 20px;  
        margin: auto;  
        
        min-height: auto;
        max-height: auto;  /* ✅ Fix: Height auto-adjust */
        
        border-radius: 10px;
        box-shadow: 2px 8px 12px rgba(5, 5, 5, 0.52);
        border: 2px solid black;
        box-sizing: border-box;
        overflow: hidden; /* ✅ Fix: Hide extra content */
}

    


   
    /* Title Styling (Now Fixed) */
    h1 {
        color: brown !important;
        font-size: 2rem;
        font-weight: bold;
        text-transform: uppercase;
        margin-bottom: 20px;
        text-align: center;
        font-family: sans-serif;
        
    }

    /* Buttons */
    div.stButton > button {
        background: linear-gradient(135deg, #00c6ff, #0072ff);
        color: white;
        font-size: 1rem;
        padding: 10px;
        border-radius: 8px;
        border: none;
        transition: 0.3s ease-in-out;
        font-weight: bold;
        text-transform: uppercase;
        cursor: pointer;
        width: 50%;
        margin-top: 10px;
        justify-content: center;
        
    }

    /* Button Hover Effect */
    div.stButton > button:hover {
        background: linear-gradient(135deg, #0072ff, #00c6ff);
        transform: scale(1.05);
    }

    /* Input Fields */
    div[data-testid="stSelectbox"] label, div[data-testid="stNumberInput"] label {
        font-size: 1rem;
        font-weight: bold;
        color:rgb(19, 18, 18);
    }

    div[data-testid="stNumberInput"] input {
        font-size: 1rem;
        padding: 8px;
        border-radius: 6px;
        border: 2px solid #ccc;
        width: 80%;
        transition: 0.3s ease-in-out;
    }

    div[data-testid="stNumberInput"] input:focus {
        border-color: #0072ff;
        box-shadow: 0px 0px 10px rgba(0, 114, 255, 0.3);
    }

    /* Success Message */
    div[data-testid="stSuccessMessage"] {
        background: linear-gradient(135deg, #4CAF50, #2E7D32);
        color: white;
        padding: 10px;
        border-radius: 8px;
        font-size: 1rem;
        font-weight: bold;
        text-align: center;
        width: 80%;
        margin-top: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ✅ Title with Fixed Coloring
st.markdown("<h1>🛰️ Astro Unit Converter</h1>", unsafe_allow_html=True)

# 🎨 Centered Card Layout
st.markdown('<div class="converter-card">', unsafe_allow_html=True)

# 🔄 Conversion dictionary
conversions = {
    "Length": {
        "Meters to Kilometers": 0.001, "Kilometers to Meters": 1000,
        "Feet to Meters": 0.3048, "Meters to Feet": 3.281,
        "Inches to Centimeters": 2.54, "Centimeters to Inches": 0.3937
    },
    "Weight": {
        "Grams to Kilograms": 0.001, "Kilograms to Grams": 1000,
        "Pounds to Kilograms": 0.4536, "Kilograms to Pounds": 2.205,
        "Ounces to Grams": 28.35, "Grams to Ounces": 0.0353
    },
    "Temperature": {
        "Celsius to Fahrenheit": lambda c: (c * 9/5) + 32,
        "Fahrenheit to Celsius": lambda f: (f - 32) * 5/9
    },
    "Time": {
        "Minutes to Hours": 1/60, "Hours to Minutes": 60,
        "Seconds to Minutes": 1/60, "Minutes to Seconds": 60
    },
    "Speed": {
        "Kilometers per Hour to Meters per Second": 0.2778,
        "Meters per Second to Kilometers per Hour": 3.6,
        "Miles per Hour to Kilometers per Hour": 1.609,
        "Kilometers per Hour to Miles per Hour": 0.6214
    },
    "Area": {
        "Square Meters to Square Kilometers": 0.000001,
        "Square Kilometers to Square Meters": 1000000,
        "Square Feet to Square Meters": 0.0929,
        "Square Meters to Square Feet": 10.764
    }
}

# 🛠 User selects conversion category
category = st.selectbox("🔄 Choose Conversion Type:", list(conversions.keys()))

# 🎯 User selects conversion option
conversion = st.selectbox("🎯 Select Conversion:", list(conversions[category].keys()))

# 🔢 User Input
value = st.number_input(f"🔢 Enter Value to Convert:", min_value=0.0, step=0.1)

# ✅ Convert and Display Result
if st.button("🔄 Convert Now"):
    if category == "Temperature":
        result = conversions[category][conversion](value)  # Function for temperature
    else:
        result = value * conversions[category][conversion]  # Multiplication for other conversions

    st.success(f"✅ Converted Value: {result:.4f}")

# 🎨 Close Card Layout
st.markdown('</div>', unsafe_allow_html=True)


