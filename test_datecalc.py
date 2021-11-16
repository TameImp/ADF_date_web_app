from datetime import datetime
from datecalc import duration, when

# basic test to ensure pytest running as expected
def test_func():
    assert 5==5

# For loop unit test to check start and end dates recognised as strings (and therefore requiring conversion to datetimes)
def test_duration():
        start_date = "21,12,2021"
        end_date = "26,12,2021"
        for obj in (start_date, end_date):
            assert isinstance(obj, str)

# Unit test 1 on "test_duration" function to test if start and end date are the same, result of the function is 0
def test_duration1():
        start_date = "21,12,2021"
        end_date = "21,12,2021"
        start_date = datetime.strptime(start_date, "%d,%m,%Y")
        end_date = datetime.strptime(end_date, "%d,%m,%Y")
        result = duration(start_date, end_date)
        assert result == 0

# Unit test 2 on "test_duration" function to test if start date = "21,12,2021" and end date = "26,12,2021" then result of function is 5
def test_duration2():
        start_date = "21,12,2021"
        end_date = "26,12,2021"
        start_date = datetime.strptime(start_date, "%d,%m,%Y")
        end_date = datetime.strptime(end_date, "%d,%m,%Y")
        result = duration(start_date, end_date)
        assert result == 5

# Unit test 3 on "test_duration" function to test if days_between is set as 0 then the result of the function is == to the start_date
def test_when1():
    start_date = "21,12,2021"
    days_between = 0
    start_date = datetime.strptime(start_date, "%d,%m,%Y")
    result = when(start_date, days_between)
    result.strftime("%d,%b,%Y")
    assert result == datetime.strptime('2021-12-21 00:00:00', "%Y-%m-%d %H:%M:%S")

# Unit test 4 on "test_duration" function to test if days_between is 5 and start_date = "21,12,2021" then result of function = '2021-12-26 00:00:00'
def test_when2():
    start_date = "21,12,2021"
    days_between = 5
    start_date = datetime.strptime(start_date, "%d,%m,%Y")
    result = when(start_date, days_between)
    result.strftime("%d,%b,%Y")
    assert result == datetime.strptime('2021-12-26 00:00:00', "%Y-%m-%d %H:%M:%S")
