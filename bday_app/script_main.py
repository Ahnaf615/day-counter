import datetime
import pytz


def time_calc(month, day):
    year = datetime.date.today().year
    bday = datetime.datetime(year, month, day, 0, 0, 0, 0, tzinfo=pytz.UTC)
    tday = datetime.datetime.now(tz=pytz.UTC)
    difference = bday - tday
    return difference.days


print(time_calc(7, 3))
