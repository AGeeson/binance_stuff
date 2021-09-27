# This script should invest money on a consistent basis for you into one stock at the best possible time within a window
import datetime
import math
import random
import time
import apirequest


hourly_moving_average = apirequest.generate_hourly_moving_average_between_dates(
    start_date, datetime.date.today()
)


def is_the_number():
    random_number = random.randint(1, 3)
    print(random_number)
    if random_number == 2:
        print("return true")
        return True
    else:
        print("return false")
        return False


def check_position_is_good(stock):
    return is_the_number()


def get_position():
    pass


def check_if_in_investment_window_days(
    days_between_investments,
    number_of_hours_to_make_investment,
    last_investment_date=None,
):
    if last_investment_date:
        next_investment_date = datetime.datetime.strftime(
            datetime.datetime.strptime(last_investment_date, "%d-%m-%Y")
            + datetime.timedelta(days=days_between_investments),
            "%d-%m-%Y",
        )
        print(f"Next investment date is : {next_investment_date}")
        print(f"Today is : {datetime.datetime.today().strftime('%d-%m-%Y')}")
        if next_investment_date == datetime.datetime.today().strftime("%d-%m-%Y"):
            return True
        else:
            return False
    else:
        return True


def make_buy(amount_to_invest):
    print("buying!")
    pass


def main(
    days_between_investments,
    number_of_hours_to_make_investment,
    stock,
    amount_to_invest,
    last_investment_date=None,
):
    if check_if_in_investment_window_days(
        days_between_investments,
        number_of_hours_to_make_investment,
        last_investment_date,
    ):
        while True:
            if check_position_is_good(stock):
                make_buy(amount_to_invest)
                break
            else:
                print("I'm sleeping")
                time.sleep(1)
    else:
        print("will check if we're in the window in an hour")
        time.sleep(3600)


main(2, 2, "BTC", 400)
