import streamlit as st
import requests

API_URL = "https://YOUR-RENDER-URL.onrender.com/predict"

# -----------------------
# SIDEBAR (App Description)
# -----------------------
st.sidebar.title("🔥 Calories Burnt App")

st.sidebar.markdown("""
This application predicts the number of calories burned during physical activity using a trained Machine Learning model.

### 🧠 How it works:
- Input your body and exercise details
- ML model processes features
- Predicts calories burned instantly

### ⚙️ Tech Stack:
- FastAPI (Backend)
- CatBoost/XGBoost Model
- Streamlit (Frontend)
- Render (Deployment)

---

Developed as a Machine Learning Engineering project.
""")

# -----------------------
# MAIN TITLE
# -----------------------
st.title("🔥 Calories Burnt Predictor")

st.markdown("Enter your details below to estimate calories burned during exercise.")

# -----------------------
# FEATURE IMPORTANCE INFO
# -----------------------
st.subheader("📊 Feature Importance (Model Insight)")

st.markdown("""
- 🏃 **Duration** → Most influential (longer exercise = more calories)
- ❤️ **Heart Rate** → Higher intensity increases burn
- ⚖️ **Weight** → Higher body weight increases energy consumption
- 📏 **Height** → Indirect metabolic factor
- 🎂 **Age** → Affects metabolic rate
- 🚻 **Gender** → Physiological differences in energy usage
- 🌡️ **Body Temperature** → Exercise intensity indicator
""")

st.divider()

# -----------------------
# TWO COLUMN INPUT UI
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
# PREDICTION BUTTON
# -----------------------
if st.button("🔥 Predict Calories"):

    payload = {
        "Gender": gender,
        "Age": age,
        "Height": height,
        "Weight": weight,
        "Duration": duration,
        "Heart_Rate": heart_rate,
        "Body_Temp": body_temp
    }

    response = requests.post(API_URL, json=payload)

    if response.status_code == 200:
        result = response.json()

        st.success(f"🔥 Estimated Calories Burned: {result['prediction']:.2f} kcal")

    else:
        st.error("Prediction failed. Please check API connection.")
        