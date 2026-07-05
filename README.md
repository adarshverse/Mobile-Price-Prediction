# 📱 Mobile Price Prediction & Recommendation System

## Overview

This project predicts smartphone prices using Machine Learning based on their specifications. It also recommends smartphones according to the user's budget and preferences through an interactive Streamlit web application.

The project demonstrates the complete Machine Learning pipeline, starting from web scraping and data preprocessing to model training, evaluation, deployment, and recommendation.

---

## Technologies Used

### Programming Language
- Python

### Web Scraping
- Selenium
- BeautifulSoup4
- Requests

### Data Processing
- Pandas
- NumPy

### Data Visualization
- Matplotlib
- Seaborn

### Machine Learning
- Scikit-learn

### Model Serialization
- Pickle

### Web Application
- Streamlit

---

## Dataset Features

The dataset was collected by scraping Flipkart smartphone listings.

### Features Used

- Brand
- Model
- Price (Target Variable)
- Rating Count
- RAM (GB)
- ROM (GB)
- Display Size (cm)
- Rear Camera (MP)
- Battery Capacity (mAh)
- Screen Type
- Color
- Processor
- Camera Details

---

## Target Variable

**Price (₹)**

---

## Project Workflow

### 1. Web Scraping
- Collected smartphone data from Flipkart
- Automated browsing using Selenium
- Parsed webpage data using BeautifulSoup

### 2. Data Cleaning
- Removed duplicate records
- Handled missing values
- Converted data into usable formats
- Extracted numerical values from text columns
- Created new useful features

### 3. Exploratory Data Analysis (EDA)
- Distribution of smartphone prices
- Brand-wise analysis
- RAM vs Price
- ROM vs Price
- Battery vs Price
- Camera vs Price
- Correlation Analysis

### 4. Feature Engineering
- Extracted:
  - RAM_GB
  - ROM_GB
  - Battery_mAh
  - Display_cm
  - Rear_Camera_MP
  - Rating_Count
- One-Hot Encoding of Brand
- Encoding of Screen Type

### 5. Model Training
- Train-Test Split
- Linear Regression Model
- Model Evaluation

### 6. Model Deployment
- Saved trained model using Pickle
- Built interactive Streamlit application
- Integrated prediction model into the web app

### 7. Phone Recommendation
- Budget-based recommendations
- RAM & ROM filtering
- Displays top matching smartphones

---

## Machine Learning Algorithm

- Linear Regression

---

## Model Performance

- **R² Score:** 0.7018
- **Mean Absolute Error (MAE):** 7797.65
- **Root Mean Squared Error (RMSE):** 11403.79

---

## Application Features

### 🏠 Home Page
- Project overview
- Technologies used
- Feature description

### 💰 Price Prediction
Predict smartphone prices using:
- Brand
- Rating Count
- RAM
- ROM
- Display Size
- Rear Camera
- Battery Capacity
- Screen Type

### 📱 Phone Recommendation
Recommend smartphones based on:
- Budget
- Minimum RAM
- Minimum ROM

---

## Project Structure

```
Mobile-Price-Prediction/
│
├── Notebook/
│   ├── DataExtraction.ipynb
│   ├── DataCleaning.ipynb
│   ├── DataCleaning2.ipynb
│   ├── EDA.ipynb
│   └── Model.ipynb
│
├── Phone_Price_Prediction/
│   ├── app.py
│   ├── model (1).csv
│   ├── price_model (1).pkl
│   ├── feature_columns (1).pkl
│   └── requirements.txt
│
└── README.md
```

---

## Future Improvements

- Include Apple smartphone data
- Improve prediction accuracy using XGBoost or Random Forest
- Add processor and camera filters in recommendation system
- Deploy on Streamlit Community Cloud
- Add smartphone image previews
- Improve UI/UX with custom themes

---

## Author

**Adarsh Shree**
