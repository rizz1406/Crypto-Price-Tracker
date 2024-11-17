from crypto_data import get_historical_data
from ui_components import display_historical_graph

def show_historical_data(crypto_id, currency='usd', days=30):
    prices = get_historical_data(crypto_id, days, currency)
    display_historical_graph(prices, currency)
