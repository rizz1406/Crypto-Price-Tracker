import streamlit as st
from crypto_data import get_crypto_price

# Function to handle price alert
def setup_price_alert(crypto_id, target_price, currency='usd'):
    current_price = get_crypto_price(crypto_id, currency)
    if current_price:
        if current_price >= target_price:
            st.warning(f"🚨 Alert: {crypto_id.capitalize()} has reached the target price of {target_price} {currency.upper()}!")
        else:
            st.info(f"{crypto_id.capitalize()} is currently at {current_price} {currency.upper()}. Target is {target_price} {currency.upper()}.")
    else:
        st.error("Error fetching data for price alert.")

# Function to display alert setup UI
def price_alert_ui(crypto_id, currency='usd'):
    target_price = st.number_input(f"Set a target price for {crypto_id.capitalize()} ({currency.upper()}):", min_value=0.0, step=0.1)
    if st.button("Set Price Alert"):
        setup_price_alert(crypto_id, target_price, currency)
