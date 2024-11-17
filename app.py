import streamlit as st
from crypto_data import get_crypto_price
from ui_components import select_crypto, select_currency, refresh_button
from historical_data import show_historical_data
from price_alert import price_alert_ui

# Main function to run the Streamlit app
def main():
    st.title("Crypto Price Tracker with Streamlit")

    # Select crypto and currency
    crypto_id = select_crypto()
    currency = select_currency()

    # Fetch and display current price
    price = get_crypto_price(crypto_id, currency)
    if price:
        st.write(f"The current price of {crypto_id.capitalize()} in {currency.upper()} is: **{price}**")
    else:
        st.error("Error fetching data. Please check your internet connection or try again later.")

    # Refresh button functionality
    if refresh_button():
        price = get_crypto_price(crypto_id, currency)
        if price:
            st.write(f"The current price of {crypto_id.capitalize()} in {currency.upper()} is: **{price}**")
        else:
            st.error("Error fetching data. Please check your internet connection or try again later.")

    # Show historical data
    st.write("---")
    st.write("### View Historical Data")
    days = st.slider("Select the number of days:", min_value=1, max_value=365, value=30)
    show_historical_data(crypto_id, currency, days)

    # Setup price alert
    st.write("---")
    st.write("### Setup Price Alert")
    price_alert_ui(crypto_id, currency)

if __name__ == "__main__":
    main()
