# Livelihood Risk Predictor

This project is a **user-friendly tool** that predicts the **vulnerability of a household** based on simple socio-economic inputs. The goal is to provide **actionable insights** for non-technical users, helping organizations or individuals identify households that may need support.

---

## Table of Contents
- [Overview](#overview)
- [How It Works](#how-it-works)
- [Input Parameters](#input-parameters)
- [Risk Levels & Examples](#risk-levels--examples)
- [Live Demo](#live-demo)
- [Screenshots](#screenshots)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Notes](#notes)

---

## Overview
The **Livelihood Risk Predictor** takes simple inputs about a household and calculates a **vulnerability score**. Based on the score, it classifies the household as **Low**, **Medium**, or **High** risk.  

This tool is designed for **social organizations, NGOs, and government agencies** to quickly identify households at risk and take action.

---

## How It Works
1. Users enter household information such as **income, shocks, health access, asset index, and education**.  
2. The tool calculates a **vulnerability score** by assigning 1 point for each of the following conditions:  
   - Low income (< 2000 ₹)  
   - High number of shocks (> 2)  
   - Poor health access (< 0.5)  
   - Low asset index (< 0.5)  
   - Low education level (< 2)  
3. Scores are then mapped to risk levels:
   - **0-1 points:** Low Risk  
   - **2-3 points:** Medium Risk  
   - **4-5 points:** High Risk  

---

## Input Parameters
| Parameter                 | Description                                | Range / Options             |
|----------------------------|--------------------------------------------|----------------------------|
| Monthly Household Income   | Total monthly income in ₹                  | 0.0 and above             |
| Shocks                     | Number of recent economic/health shocks   | 0 to 5                     |
| Health Access              | Access to healthcare (0 = poor, 1 = excellent) | 0.0 to 1.0              |
| Household Asset Index      | Overall household assets (0 = low, 1 = high) | 0.0 to 1.0              |
| Education Level            | Education level of household head (0 = None, 4 = College+) | 0 to 4             |

---

## Risk Levels & Examples
The vulnerability **score** determines the risk:

| Example | Income (₹) | Shocks | Health Access | Asset Index | Education | Score | Predicted Risk |
|---------|------------|--------|---------------|-------------|-----------|-------|----------------|
| High Risk | 1000 | 4 | 0.3 | 0.2 | 0 | 5 | High |
| Medium Risk | 1800 | 3 | 0.8 | 0.9 | 3 | 2 | Medium |
| Low Risk | 3500 | 0 | 1.0 | 1.0 | 4 | 0 | Low |

**Explanation:**  
- The score is calculated by **adding 1 for each condition** that applies (low income, high shocks, poor health, low asset, low education).  
- The higher the score, the **higher the household’s vulnerability**.

---

## Live Demo
You can access the interactive demo here:  
[**Livelihood Risk Predictor Live Demo**](https://livelihood-risk-38mfu8hsjrmrkpmymcqxjt.streamlit.app/)

---

## Screenshots
### Dashboard and Predictions
![Screenshot1](images/Screenshot1.pdf)  
![Screenshot2](images/Screenshot2.pdf)  
![Screenshot3](images/Screenshot3.pdf)  

> The screenshots show how to input household data and view the predicted risk level with simple guidance.

---

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/livelihood-risk-predictor.git
cd livelihood-risk-predictor

Install required packages:
streamlit run dashboard/streamlit-app.py
Enter household data in the fields.

Click Predict.

The tool will display the risk level and provide simple guidance.

API (Optional)

If you want to use the API:

uvicorn api/main:app --reload


POST request to /predict with JSON body:

{
  "income": 2000,
  "shocks": 2,
  "health_access": 0.5,
  "asset_index": 0.7,
  "education_level": 2
}

Project Structure
├── api/
│   └── main.py              # FastAPI endpoints
├── dashboard/
│   └── streamlit-app.py     # Streamlit dashboard
├── data/
│   ├── fetched_data.csv
│   └── raw_data.csv
├── images/
│   ├── screenshot1.pdf
│   ├── screenshot2.pdf
│   └── screenshot3.pdf
├── model.pkl
├── model_train.py
├── clean_data.py
├── fake-api.py
├── fetch_data.py
├── requirements.txt
├── Dockerfile
└── run_project.bat

Notes

The thresholds are illustrative to demonstrate how socio-economic factors affect household vulnerability.

This project is ideal for NGOs, social researchers, and government agencies who want a quick assessment tool.

All users can interact with it without coding knowledge.
