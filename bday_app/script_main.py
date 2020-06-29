import datetime
import pytz


def time_calc(month, day, year):
    # year = datetime.date.today().year
    target_date = datetime.datetime(year, month, day, 0, 0, 0, 0, tzinfo=pytz.UTC)
    tday = datetime.datetime.now(tz=pytz.UTC)
    difference = target_date - tday
    return difference.days


