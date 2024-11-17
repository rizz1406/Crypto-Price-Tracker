import streamlit as st

# Function to display dropdown for selecting crypto
def select_crypto():
    # Top 20 cryptocurrencies (based on market capitalization)
    crypto_options = {
        'Bitcoin': 'bitcoin',
        'Ethereum': 'ethereum',
        'Tether': 'tether',
        'BNB': 'binancecoin',
        'XRP': 'ripple',
        'Cardano': 'cardano',
        'Dogecoin': 'dogecoin',
        'Polygon': 'matic-network',
        'Solana': 'solana',
        'Polkadot': 'polkadot',
        'Litecoin': 'litecoin',
        'Avalanche': 'avalanche-2',
        'Chainlink': 'chainlink',
        'Uniswap': 'uniswap',
        'Cosmos': 'cosmos',
        'Toncoin': 'toncoin',
        'Stellar': 'stellar',
        'Monero': 'monero',
        'Ethereum Classic': 'ethereum-classic',
        'Internet Computer': 'internet-computer'
    }
    selected_crypto = st.selectbox("Choose a Cryptocurrency:", list(crypto_options.keys()))
    return crypto_options[selected_crypto]

# Function to display dropdown for selecting currency
def select_currency():
    # Restricting to INR and USD
    currency_options = ['usd', 'inr']
    return st.selectbox("Choose a Currency:", currency_options)

# Function to display a refresh button
def refresh_button():
    return st.button("Refresh Price")

# Function to show historical data graph
def display_historical_graph(prices, currency='usd'):
    import pandas as pd
    import matplotlib.pyplot as plt

    if prices:
        df = pd.DataFrame(prices, columns=['Timestamp', 'Price'])
        df['Date'] = pd.to_datetime(df['Timestamp'], unit='ms')
        df.set_index('Date', inplace=True)

        # Plotting the graph
        st.write("### Historical Price Data")
        st.line_chart(df['Price'])
