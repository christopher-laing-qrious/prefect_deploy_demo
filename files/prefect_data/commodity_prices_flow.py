import requests
from prefect import flow, task
import sqlite3
from datetime import datetime

@task
def fetch_commodity_prices():
    url = "https://www.goldapi.io/api/XAU/USD"
    headers = {"x-access-token": "your_api_key_here"}
    
    response = requests.get(url, headers=headers)
    data = response.json()
    
    print("Received data:", data)  # Add this line to print the received data
    
    try:
        return {
            "date": datetime.fromtimestamp(data.get("timestamp", 0)),
            "price": data.get("price", 0),
            "currency": data.get("currency", "USD"),
            "commodity": "Gold"
        }
    except KeyError as e:
        print(f"KeyError: {e} not found in the data")
        return None

@task
def store_in_sqlite(data):
    if data is None:
        print("No data to store")
        return
    
    conn = sqlite3.connect('commodity_prices.db')
    c = conn.cursor()
    
    c.execute('''CREATE TABLE IF NOT EXISTS prices
                 (date text, price real, currency text, commodity text)''')
    
    c.execute("INSERT INTO prices VALUES (?,?,?,?)", 
              (data['date'], data['price'], data['currency'], data['commodity']))
    
    conn.commit()
    conn.close()

@flow
def commodity_prices_to_sqlite():
    data = fetch_commodity_prices()
    if data:
        store_in_sqlite(data)
    else:
        print("Failed to fetch commodity prices")

if __name__ == "__main__":
    commodity_prices_to_sqlite()
