@echo off
echo 🔁 Activating virtual environment...
call venv\Scripts\activate

echo 📥 Fetching data from fake API...
python fetch_data.py

echo 🧹 Cleaning data...
python clean_data.py

echo 🤖 Training model...
python model_train.py


