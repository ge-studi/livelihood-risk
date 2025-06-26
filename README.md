# 🧠 Livelihood Risk Predictor

A machine learning-powered Streamlit web app that predicts **household vulnerability score** based on income, shocks, health access, asset index, and education level. Built with FastAPI + XGBoost + SHAP for model explainability.
## 🔍 SHAP Summary Plot

This plot shows feature importance using SHAP values:

![SHAP Summary](shap_summary.png)

![Livelihood Risk Predictor UI](screenshot1.png)
![Livelihood Risk Predictor UI](screenshot2.png)
---

## 🚀 Project Features

- 📡 **Fake API** to simulate real-world household data
- 🔍 **Data cleaning** and preprocessing pipeline
- 🎯 **XGBoost Classifier** to predict vulnerability
- 🔎 **SHAP analysis** for explainability
- 🌐 **FastAPI endpoint** for predictions (`/predict`)
- 📊 **Streamlit dashboard** for user-friendly input & score

---

## 📁 Folder Structure

<pre> 📦 livelihood-risk 
  ├── 📁 api
  │ └── 📄 main.py # FastAPI prediction endpoint
  ├── 📁 dashboard 
  │ └── 📄 streamlit-app.py # Streamlit frontend for input and prediction 
  ├── 📁 data 
  │ ├── 📄 raw_data.csv # Raw data from fake API
  │ └── 📄 fetched_data.csv # Cleaned data used for training 
  ├── 📄 fake_api.py # Fake API to simulate household data 
  ├── 📄 fetch_data.py # Script to fetch and save fake data
  ├── 📄 clean_data.py # Script to clean and preprocess data
  ├── 📄 model_train.py # Trains XGBoost model and saves model.pkl 
  ├── 📄 run_project.bat # Batch script to run the full pipeline 
  ├── 📄 requirements.txt # Python dependencies 
  ├── 📄 Dockerfile # Docker setup  
  ├── 📄 .gitignore # Git ignore rules 
  ├── 📄 README.md # Project documentation
  ├── 📄 model.pkl # Trained model (optional to track in Git) 
  ├── 🖼️ screenshot1.png # Screenshot of Streamlit UI 
  ├── 🖼️ screenshot2.png # Screenshot of prediction output 
  └── 🖼️ shap_summary.png # SHAP interpretability plot </pre>



---

## ⚙️ Setup Instructions

### 1. Clone Repo & Set Up Virtual Environment

```bash
git clone https://github.com/your-username/livelihood-risk.git
cd livelihood-risk
python -m venv venv
venv\Scripts\activate  # On Windows
pip install -r requirements.txt
2. Start Fake API (Terminal 1)
venv\Scripts\activate
python -m uvicorn fake_api:app --reload --port 8000
3. Run Project Setup (Terminal 2)
venv\Scripts\activate
./run_project.bat
4. Start Prediction API (Terminal 3)
venv\Scripts\activate
python -m uvicorn api.main:app --reload --port 8500
5. Run Streamlit Dashboard (Terminal 4)
venv\Scripts\activate
streamlit run dashboard/streamlit-app.py
📡 API Endpoints
GET /get_data → from fake_api.py

POST /predict → returns vulnerability score
POST http://localhost:8500/predict
{
  "income": 1000,
  "shocks": 2,
  "health_access": 0.7,
  "asset_index": 0.5,
  "education_level": 3
}
Response:

{ "vulnerability_score": 1 }
🛡️ Tech Stack
Python

FastAPI

Streamlit

XGBoost

SHAP

Pandas, NumPy

🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first.
