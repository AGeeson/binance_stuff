import json
from binance.client import Client
import config
import datetime

today = datetime.date.today()
tomorrow = datetime.date.today() + datetime.timedelta(days=1)
five_days_ago = datetime.date.today() - datetime.timedelta(days=5)


api_key = config.binance["api_key"]
secret_key = config.binance["secret_key"]

client = Client(api_key, secret_key, {"verify": False, "timeout": 20})
# print(client.get_all_orders(symbol='BNBBTC', requests_params={'timeout': 5}))

# print(client.get_historical_klines("BNBBTC", Client.KLINE_INTERVAL_1MINUTE, "1 day ago UTC"))


avg_price = client.get_avg_price(symbol="BNBBTC")
# print(avg_price)


def get_market_data_days(start_date, end_date):
    print(
        client.get_historical_klines(
            "BNBBTC", Client.KLINE_INTERVAL_1DAY, "2021-08-07", "2021-08-08"
        )
    )
    return client.get_historical_klines(
        "BNBBTC", Client.KLINE_INTERVAL_1DAY, "2021-08-07", "2021-08-08"
    )


def get_market_data_hours(start_date, end_date):
    """Format date as such: 2021-09-28"""
    try:
        return client.get_historical_klines(
            "BNBBTC", Client.KLINE_INTERVAL_1HOUR, start_date, end_date
        )
    except Exception as e:
        print(e)
        raise (e)


def calculate_moving_average(data=list):
    return sum(data) / len(data)


def convert_unix_to_datetime(ts):
    return datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")


def generate_hourly_moving_average_between_dates(start_date, end_date):
    """if you get tomorrow's date as the end_date the last datapoint will be the most recent datapoint
    also the unix time contains milliseconds so they have to stripped when converting it to utc"""
    hourly_data = get_market_data_hours(start_date, end_date)

    hourly_output = []
    hourly_output_non_unix = []
    for hour in hourly_data:
        hourly_output.append(float(hour[2]))
        hourly_output_non_unix.append(convert_unix_to_datetime(int(str(hour[0])[:-3])))

    print(hourly_output)

    hourly_moving_av = calculate_moving_average(hourly_output)

    print(f"this be the moving average: {str(hourly_moving_av)}")

    print(hourly_output_non_unix)
    return hourly_moving_av


generate_hourly_moving_average_between_dates("2021-09-26", "2021-09-27")


def is_stock_rn_below_moving_average():
    ma = generate_hourly_moving_average_between_dates(str(five_days_ago), str(tomorrow))
    last_hour_high = float(
        get_market_data_hours(str(five_days_ago), str(tomorrow))[-1:][0][2]
    )
    print(ma)
    print(last_hour_high)
    outcome = True if last_hour_high < ma else False
    print(outcome)
    return outcome


is_stock_rn_below_moving_average()


# print(f"this be the len: {len(get_market_data_hours())}")
# data = json.dumps(get_market_data_days())

# with open("data.txt", "w") as outfile:
# json.dump(data, outfile)

# [
#   [
#     1499040000000,      // Open time
#     "0.01634790",       // Open
#     "0.80000000",       // High
#     "0.01575800",       // Low
#     "0.01577100",       // Close
#     "148976.11427815",  // Volume
#     1499644799999,      // Close time
#     "2434.19055334",    // Quote asset volume
#     308,                // Number of trades
#     "1756.87402397",    // Taker buy base asset volume
#     "28.46694368",      // Taker buy quote asset volume
#     "17928899.62484339" // Ignore
#   ]
# ]
