from datetime import datetime
from datecalc import duration, when

def test_func():
    assert 5==5

def test_duration():
        start_date = "21,12,2021"
        end_date = "26,12,2021"
        for obj in (start_date, end_date):
            assert isinstance(obj, str)

def test_duration1():
        start_date = "21,12,2021"
        end_date = "21,12,2021"
        start_date = datetime.strptime(start_date, "%d,%m,%Y")
        end_date = datetime.strptime(end_date, "%d,%m,%Y")
        result = duration(start_date, end_date)
        assert result == 0

def test_duration2():
        start_date = "21,12,2021"
        end_date = "26,12,2021"
        start_date = datetime.strptime(start_date, "%d,%m,%Y")
        end_date = datetime.strptime(end_date, "%d,%m,%Y")
        result = duration(start_date, end_date)
        assert result == 5

def test_when1():
    start_date = "21,12,2021"
    days_between = 0
    start_date = datetime.strptime(start_date, "%d,%m,%Y")
    result = when(start_date, days_between)
    result.strftime("%d,%b,%Y")
    assert result == datetime.strptime('2021-12-21 00:00:00', "%Y-%m-%d %H:%M:%S")

def test_when2():
    start_date = "21,12,2021"
    days_between = 5
    start_date = datetime.strptime(start_date, "%d,%m,%Y")
    result = when(start_date, days_between)
    result.strftime("%d,%b,%Y")
    assert result == datetime.strptime('2021-12-26 00:00:00', "%Y-%m-%d %H:%M:%S")


# test_duration("21,12,2021", "22,12,2021")


# # test if data types in 
# def test_app_dtype():
#     start_date = '20-10-2017'
#     end_date = '20-10-2018'
    
#     # duration(start_date, end_date)
#     # assert isinstance(start_date,str)

# # number = 10
# # print(isinstance(number,int))
#     print(type(duration))

# print(isinstance(duration(10,11,str))