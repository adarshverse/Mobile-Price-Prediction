import streamlit as st
import pandas as pd
import pickle

with open("price_model (1).pkl", "rb") as f:
    model = pickle.load(f)

with open("feature_columns (1).pkl", "rb") as f:
    feature_columns = pickle.load(f)

df = pd.read_csv("model (1).csv")

st.sidebar.title("📱 Navigation")

page = st.sidebar.radio(
    "Go To",
    ["🏠 Home", "💰 Price Prediction", "📱 Phone Recommendation"]
)

if page == "🏠 Home":

    st.title("📱 Mobile Price Prediction & Recommendation System")

    st.image(
        "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=900"
    )

    st.markdown("---")

    st.header("About Project")

    st.write("""
This project predicts smartphone prices using Machine Learning.

### Features
- 💰 Predict Mobile Price
- 📱 Recommend Phones within Budget
- ⚡ Fast Prediction
- 🤖 Machine Learning Model

### Technologies Used
- Python
- Pandas
- Scikit-learn
- Streamlit

### Developed By
Adarsh Shree
""")

elif page == "💰 Price Prediction":

    st.title("💰 Mobile Price Prediction")

    brand = st.selectbox(
        "Brand",
        [
            "AI+","ALCATEL","COOLPAD","GOOGLE","HMD","INFINIX","IQOO",
            "ITEL","LAVA","LENOVO","MI","MOTOROLA","NOTHING","ONEPLUS",
            "OPPO","POCO","REALME","REDMI","SAMSUNG","SIAVANTAGE",
            "TECNO","VIVO","XIAOMI","XOME"
        ]
    )

    rating_count = st.number_input("Rating Count",0,500000,1000)

    ram = st.selectbox("RAM (GB)",[2,4,6,8,12,16])

    rom = st.selectbox("ROM (GB)",[32,64,128,256,512,1024])

    display = st.number_input("Display Size (cm)",value=16.5)

    camera = st.number_input("Rear Camera (MP)",value=50.0)

    battery = st.number_input("Battery (mAh)",value=5000)

    screen = st.selectbox(
        "Screen Type",
        ["AMOLED","LCD","OLED","Other"]
    )

    if st.button("Predict Price"):

        data = {col:0 for col in feature_columns}

        data["Rating_Count"] = rating_count
        data["RAM_GB"] = ram
        data["ROM_GB"] = rom
        data["Display_cm"] = display
        data["Rear_Camera_MP"] = camera
        data["Battery_mAh"] = battery

        brand_col = f"Brand_{brand}"

        if brand_col in data:
            data[brand_col] = 1

        if screen == "Other":
            data["Screen_Type_Other"] = 1

        input_df = pd.DataFrame([data])

        prediction = round(model.predict(input_df)[0])

        st.success(f"💰 Estimated Price : ₹{prediction:,}")

        st.balloons()

elif page == "📱 Phone Recommendation":

    st.title("📱 Phone Recommendation")

    budget = st.slider(
        "Select Your Budget",
        5000,
        100000,
        30000,
        step=1000
    )

    ram = st.selectbox(
        "Minimum RAM",
        sorted(df["RAM_GB"].unique())
    )

    rom = st.selectbox(
        "Minimum ROM",
        sorted(df["ROM_GB"].unique())
    )

    phones = df[
        (df["Price"] <= budget) &
        (df["RAM_GB"] >= ram) &
        (df["ROM_GB"] >= rom)
    ]

    phones = phones.sort_values(
        "Rating_Count",
        ascending=False
    )

    st.subheader("Recommended Phones")

    if len(phones) == 0:
        st.error("No Phones Found")

    else:
        st.dataframe(
            phones[
                [
                    "Brand",
                    "Model",
                    "Price",
                    "RAM_GB",
                    "ROM_GB",
                    "Battery_mAh"
                ]
            ].head(10)
        )
        
        #streamlit run app.py