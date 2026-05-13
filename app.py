import streamlit as st
import requests

API_URL = "https://calorie-predictor-api.onrender.com/predict"

# -----------------------
# SIDEBAR
# -----------------------
st.sidebar.title("🔥 Calories Burnt App")

st.sidebar.markdown("""
This application predicts calories burned during physical activity using a trained ML model.

### 🧠 How it works:
- Enter your body & exercise details
- Data is sent to FastAPI backend
- ML model predicts calories burned
- Result is displayed instantly

### ⚙️ Tech Stack:
- FastAPI (Backend)
- Streamlit (Frontend)
- CatBoost Model
- Render (Deployment)

---
Built as an ML Engineering project.
""")

# -----------------------
# TITLE
# -----------------------
st.title("🔥 Calories Burnt Predictor")
st.markdown("Enter your details below to predict calories burned.")

# -----------------------
# FEATURE INSIGHT
# -----------------------
st.subheader("📊 Feature Importance Insight")

st.markdown("""
- 🏃 Duration → most important factor  
- ❤️ Heart Rate → intensity indicator  
- ⚖️ Weight → energy consumption  
- 📏 Height → metabolic factor  
- 🎂 Age → affects metabolism  
- 🚻 Gender → physiological variation  
- 🌡️ Body Temp → exercise intensity  
""")

st.divider()

# -----------------------
# INPUT UI
# -----------------------
col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["male", "female"])
    age = st.number_input("Age", 1, 100, 25)
    height = st.number_input("Height (cm)", 100, 250, 170)
    weight = st.number_input("Weight (kg)", 30, 200, 70)

with col2:
    duration = st.number_input("Exercise Duration (min)", 1, 300, 30)
    heart_rate = st.number_input("Heart Rate", 50, 200, 100)
    body_temp = st.number_input("Body Temperature (°C)", 30.0, 45.0, 37.0)

# -----------------------
# PREDICTION
# -----------------------
if st.button("🔥 Predict Calories"):

    # FIX 1: encode gender properly
    gender_encoded = 0 if gender == "male" else 1

    payload = {
        "Gender": gender_encoded,
        "Age": age,
        "Height": height,
        "Weight": weight,
        "Duration": duration,
        "Heart_Rate": heart_rate,
        "Body_Temp": body_temp
    }

    try:
        response = requests.post(API_URL, json=payload)

        # DEBUG (important for deployment troubleshooting)
        if response.status_code != 200:
            st.error(f"Backend Error: {response.status_code}")
            st.write(response.text)
        else:
            result = response.json()

            # FIX 2: correct key from backend
            prediction = result.get("Predicted calories burnt", None)

            if prediction is not None:
                st.success(f"🔥 Estimated Calories Burned: {prediction:.2f} kcal")
            else:
                st.error("Prediction key not found in response")
                st.write(result)

    except Exception as e:
        st.error("Request failed. Cannot connect to API.")
        st.exception(e)