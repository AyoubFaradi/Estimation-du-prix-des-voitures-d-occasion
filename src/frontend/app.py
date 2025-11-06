import streamlit as st
import requests
import pandas as pd
import os

API_URL = os.getenv("API_URL", "http://localhost:8000/predict")

st.title("🚗 Estimation du prix d'une voiture d'occasion")
st.write("Remplissez les informations pour obtenir une estimation en MAD")

company = st.selectbox("Marque", ["Maruti", "Hyundai", "Toyota", "Ford", "BMW"])
model = st.text_input("Modèle")
edition = st.text_input("Édition")
year = st.number_input("Année", 1990, 2025, 2018)
owner = st.selectbox("Propriétaire", ["First", "Second", "Third","hassan"])
fuel = st.selectbox("Carburant", ["Petrol", "Diesel", "CNG", "LPG", "Electric"])
seller_type = st.selectbox("Type de vendeur", ["Individual", "Dealer"])
transmission = st.selectbox("Transmission", ["Manual", "Automatic"])
km_driven = st.number_input("Kilométrage", 0, 300000, 50000)
mileage_mpg = st.number_input("Consommation (mpg)", 0.0, 50.0, 20.0)
engine_cc = st.number_input("Cylindrée (cc)", 500.0, 5000.0, 1500.0)
max_power_bhp = st.number_input("Puissance (bhp)", 30.0, 500.0, 100.0)
torque_nm = st.number_input("Couple (Nm)", 50.0, 600.0, 150.0)
seats = st.number_input("Nombre de sièges", 2, 10, 5)

if st.button("Prédire le prix 💰"):
    payload = {
        "company": company, "model": model, "edition": edition,
        "year": year, "owner": owner, "fuel": fuel,
        "seller_type": seller_type, "transmission": transmission,
        "km_driven": km_driven, "mileage_mpg": mileage_mpg,
        "engine_cc": engine_cc, "max_power_bhp": max_power_bhp,
        "torque_nm": torque_nm, "seats": seats
    }
    response = requests.post(API_URL, json=payload)
    if response.status_code == 200:
        price = response.json()["estimated_price_MAD"]
        st.success(f"💸 Prix estimé : {price} MAD")
    else:
        st.error("Erreur lors de la prédiction.")
