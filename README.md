# 💰 Insurance Cost Prediction — Machine Learning with FastAPI & Streamlit

## 📘 Overview  
This project is a **learning-based implementation** of a **Machine Learning model** for predicting medical insurance costs based on multiple factors such as age, BMI, region, and smoking habits.  
The primary goal was to explore how to **train, deploy, and interact with an ML model** using **FastAPI** as a backend and **Streamlit** as a user-friendly web interface.

---

## 🎯 Project Objectives
- Understand end-to-end ML deployment.
- Learn integration between **FastAPI** (for backend) and **Streamlit** (for frontend).
- Practice **pickle model storage** and **API serving**.
- Implement **real-time prediction requests** using `requests` library.

---

## ⚙️ Tech Stack
| Category | Tools Used |
|-----------|-------------|
| **Programming Language** | Python 3 |
| **Backend Framework** | FastAPI, Uvicorn, Pyngrok |
| **Frontend Framework** | Streamlit |
| **Machine Learning** | Scikit-learn, Pandas, NumPy |
| **Model Persistence** | Pickle |
| **Visualization** | Seaborn, Matplotlib |

---

## 🧠 Workflow Summary
1️⃣ **Data Preprocessing** – Loaded and cleaned the insurance dataset.  
2️⃣ **Model Training** – Used **Linear Regression** to predict insurance costs.  
3️⃣ **Model Evaluation** – Achieved an R² score of ~0.75 on training and testing data.  
4️⃣ **Model Deployment** – Created a **FastAPI endpoint** `/Insurance_prediction` for real-time predictions.  
5️⃣ **User Interface** – Built a **Streamlit app** for input and output visualization.  
6️⃣ **Integration** – Connected FastAPI and Streamlit using **HTTP POST requests**.  

---

## 📁 Project Structure
```bash
insurance_prediction_project/
│
├── data/
│   └── insurance.csv                 # Dataset file
│
├── model/
│   └── insurance.sav                 # Saved ML model (pickle format)
│
├── backend/
│   └── main_api.py                   # FastAPI backend for predictions
│
├── frontend/
│   └── insurance_streamlit_UI.py     # Streamlit UI for user interaction
│
├── training/
│   └── model_training.py             # Model training and serialization
│
└── README.md                         # Project documentation file
