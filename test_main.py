import main
from freezegun import freeze_time

@freeze_time("2021-09-23")
def test_check_if_in_investment_window_days():
    assert main.check_if_in_investment_window_days(5, 5) == True
    assert main.check_if_in_investment_window_days(2,2, "30-11-2017") == False
    assert main.check_if_in_investment_window_days(2,2, "21-09-2021") == True