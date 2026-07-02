# 🌍 African Economic GDP Predictor
**"Africa's Numbers Don't Lie. But They Don't Tell the Whole Story Either."**

An end-to-end Machine Learning pipeline predicting African GDP growth trends using World Bank macroeconomic data. Built as a Capstone Project for the AnalystLab Africa Data Science Internship.

## 📊 Project Overview
This project investigates whether traditional macroeconomic indicators (like inflation, debt, and agricultural GDP) can accurately forecast economic trajectories across 54 African nations. The final output is a deployed web application that allows users to input economic metrics and receive an instant GDP growth estimation.

## 🗂️ Repository Structure
* `african_countries_GDP_predictor.py`: The Streamlit web application code (Front-end).
* `gdp_model_pipeline.pkl`: The serialized scikit-learn machine learning pipeline (Data Preprocessor + Gradient Boosting Model).
* `requirements.txt`: The list of Python dependencies required to run the environment.
* `African Economic GDP Predictor (Capstone Project).ipynb`: The Jupyter Notebook containing the full EDA, data cleaning, and model training processes.

## 🚀 How to Run Locally
1. Clone this repository to your local machine.
2. Open your terminal or command prompt in the project folder.
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
