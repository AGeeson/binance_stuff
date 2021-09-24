from binance.client import Client

api_key = "api_key"
secret_key = "secret_key"

client = Client(api_key, secret_key, {"verify": False, "timeout": 20})
# print(client.get_all_orders(symbol='BNBBTC', requests_params={'timeout': 5}))

# print(client.get_historical_klines("BNBBTC", Client.KLINE_INTERVAL_1MINUTE, "1 day ago UTC"))


avg_price = client.get_avg_price(symbol='BNBBTC')
# print(avg_price)


def get_market_data_days():
    print(client.get_historical_klines("BNBBTC", Client.KLINE_INTERVAL_1DAY, "2021-08-07"))

def calculate_moving_average(data=list):
    return sum(data)/len(data)
    
get_market_data_days()