import requests
import time

# Function to get the current price of a cryptocurrency with retry logic
def get_crypto_price(crypto_id, currency='usd', retries=3, delay=2):
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies={currency}'
    
    for attempt in range(retries):
        try:
            response = requests.get(url)
            
            if response.status_code == 200:
                data = response.json()
                return data[crypto_id][currency]
            else:
                print(f"Attempt {attempt+1}: Failed to fetch data, status code {response.status_code}")
        
        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt+1}: Error occurred - {e}")
        
        # Wait before retrying
        time.sleep(delay)
    
    # Return None if all attempts fail
    return None

# Function to get historical data for a cryptocurrency with retry logic
def get_historical_data(crypto_id, days=30, currency='usd', retries=3, delay=2):
    url = f'https://api.coingecko.com/api/v3/coins/{crypto_id}/market_chart?vs_currency={currency}&days={days}'
    
    for attempt in range(retries):
        try:
            response = requests.get(url)
            
            if response.status_code == 200:
                data = response.json()
                prices = data['prices']
                return prices  # List of [timestamp, price]
            else:
                print(f"Attempt {attempt+1}: Failed to fetch historical data, status code {response.status_code}")
        
        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt+1}: Error occurred - {e}")
        
        # Wait before retrying
        time.sleep(delay)
    
    # Return None if all attempts fail
    return None
