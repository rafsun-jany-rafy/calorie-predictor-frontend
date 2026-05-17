# 🔥 Calories Burnt Prediction - Frontend (Streamlit UI)

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red)
![FastAPI](https://img.shields.io/badge/API-Connected-green)
![UI](https://img.shields.io/badge/Interface-Interactive-orange)
![Status](https://img.shields.io/badge/Status-Production%20Ready-success)

---

## 🚀 Project Overview

This is a **Streamlit-based frontend application** for the Calories Burnt Prediction system.

It provides an interactive web interface where users input physical activity data and receive real-time predictions from a deployed FastAPI backend.

---

## 🌐 Live Demo

[Click here to open the app][https://calorie-predictor-frontend.streamlit.app/]


## 🧠 System Architecture

User (Browser)  
↓  
Streamlit Frontend  
↓  
FastAPI Backend (Render)  
↓  
Machine Learning Model (CatBoost / XGBoost / RandomForest)  
↓  
Prediction Response  
↓  
Displayed in UI  

---

## ✨ Features

- 🎯 Interactive Streamlit UI  
- 📡 Real-time API integration  
- 🧠 ML-based prediction system  
- 📊 Structured input form  
- 🧾 Sidebar with app description  
- ⚡ Instant prediction output  
- 🌐 Connected to deployed backend API  

---

## 📊 Input Features

- Gender  
- Age  
- Height  
- Weight  
- Duration (minutes)  
- Heart Rate  
- Body Temperature  

---

## 🏗️ Tech Stack

- Python  
- Streamlit  
- Requests  
- FastAPI (Backend API)  
- Render (Deployment)  

---

## 📁 Project Structure
```text
calories_burnt_frontend/
│
├── app.py
├── requirements.txt
├── LICENSE
└── README.md
```

## ⚙️ How It Works

1. User opens Streamlit web app  
2. User enters input values in UI  
3. Streamlit sends request to FastAPI backend  
4. Backend processes input using ML model  
5. Model returns predicted calories  
6. Streamlit displays result on screen  

---

## 🚀 Run Locally

### 1. Install dependencies

```bash
pip install -r requirements.txt
```
---

### 2. Start Streamlit app
```bash
streamlit run app.py 
```
---

### 3. Open in browser
```bash
http://localhost:8501  
```
---

## 🌐Backend API

This frontend connects to:

https://calorie-predictor-api.onrender.com/predict

https://calorie-predictor-api.onrender.com/docs

---
## 🚨 Important Notes
- Backend must be running for predictions
- Ensure correct input format matching API schema
- First request may be slow due to Render cold start
- Update API URL in app.py if backend changes
---



## 🚀 Future Improvements

- Add charts for input vs prediction visualization
- Add feature importance display (from backend model)
- Improve UI with multi-page navigation
- Add authentication for personalized usage
- Deploy on Streamlit Cloud or Render 

---

## 👨‍💻 Author

Frontend component of a full-stack Machine Learning system demonstrating:

- ML model deployment
- API integration
- Interactive UI development
- End-to-end system design
---

## 📜 License

This project is licensed under the MIT License.

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub.