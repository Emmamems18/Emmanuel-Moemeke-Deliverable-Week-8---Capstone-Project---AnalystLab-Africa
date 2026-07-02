import streamlit as st
import pandas as pd
import joblib

# 1. Load the saved pipeline
pipeline = joblib.load('gdp_model_pipeline.pkl')

# 2. Full mapping of all 54 African countries and their codes
african_countries = {
    'Algeria': 'DZA', 'Angola': 'AGO', 'Benin': 'BEN', 'Botswana': 'BWA',
    'Burkina Faso': 'BFA', 'Burundi': 'BDI', 'Cape Verde': 'CPV', 'Cameroon': 'CMR',
    'Central African Republic': 'CAF', 'Chad': 'TCD', 'Comoros': 'COM',
    'Democratic Republic of Congo': 'COD', 'Republic of Congo': 'COG',
    'Djibouti': 'DJI', 'Egypt': 'EGY', 'Equatorial Guinea': 'GNQ',
    'Eritrea': 'ERI', 'Eswatini': 'SWZ', 'Ethiopia': 'ETH', 'Gabon': 'GAB',
    'Gambia': 'GMB', 'Ghana': 'GHA', 'Guinea': 'GIN', 'Guinea-Bissau': 'GNB',
    'Ivory Coast': 'CIV', 'Kenya': 'KEN', 'Lesotho': 'LSO', 'Liberia': 'LBR',
    'Libya': 'LBY', 'Madagascar': 'MDG', 'Malawi': 'MWI', 'Mali': 'MLI',
    'Mauritania': 'MRT', 'Mauritius': 'MUS', 'Morocco': 'MAR', 'Mozambique': 'MOZ',
    'Namibia': 'NAM', 'Niger': 'NER', 'Nigeria': 'NGA', 'Rwanda': 'RWA',
    'Sao Tome and Principe': 'STP', 'Senegal': 'SEN', 'Seychelles': 'SYC',
    'Sierra Leone': 'SLE', 'South Africa': 'ZAF', 'Somalia': 'SOM',
    'South Sudan': 'SSD', 'Sudan': 'SDN', 'Tanzania': 'TZA', 'Togo': 'TGO',
    'Tunisia': 'TUN', 'Uganda': 'UGA', 'Zambia': 'ZMB', 'Zimbabwe': 'ZWE'
}

# 3. Build the Streamlit App Interface
st.title("🌍 African Economic GDP Predictor")
st.write("Enter the macroeconomic indicators below to predict the GDP growth of an African nation.")

# Country Selection via Dropdown
st.header("Country Information")
col1, col2 = st.columns(2)

with col1:
    selected_country = st.selectbox("Country Name", options=list(african_countries.keys()))

with col2:
    selected_code = african_countries[selected_country]
    st.text_input("Country Code", value=selected_code, disabled=True)

# Macroeconomic Indicators
st.header("Macroeconomic Indicators")
col3, col4 = st.columns(2)

with col3:
    agri_gdp = st.number_input("Agriculture GDP (%)", value=20.0)
    edu_gni = st.number_input("Education GNI", value=3.5)
    ext_debt = st.number_input("External Debt GNI", value=40.0)
    fdi_gdp = st.number_input("FDI GDP", value=2.0)

with col4:
    inflation = st.number_input("Inflation Rate (%)", value=10.0)
    trade_gdp = st.number_input("Trade GDP", value=30.0)
    debt_gni = st.number_input("Debt GNI", value=50.0)

# 4. Prediction Button
if st.button("Predict GDP Growth"):
    input_data = pd.DataFrame({
        'Country': [selected_country],
        'Code': [selected_code],
        'Agriculture_GDP': [agri_gdp],
        'Education_GNI': [edu_gni],
        'Externaldebt_GNI': [ext_debt],
        'FDI_GDP': [fdi_gdp],
        'Inflation': [inflation],
        'Trade_GDP': [trade_gdp],
        'Debt_GNI': [debt_gni]
    })

    prediction = pipeline.predict(input_data)[0]

    st.success(f"📈 Predicted GDP Growth: {prediction:.2f}%")
    st.warning("Note: Model has an expected error margin (RMSE) of ±5.16%.")