
from datetime import datetime, timedelta

# calculates the difference between two dates in days
def duration1(start_date, end_date):
    # return abs((end_date - start_date).days)
    # print(isinstance(start_date,str))
    # print(isinstance(end_date,str))
    print(type(start_date))
    print(type(end_date))

duration1('20-02-2019','20-02-2020')
