from datetime import datetime, timedelta, date, time

from babel.dates import (
    format_datetime, 
    format_date,
)

DATE_SHORT_FORMAT = r"%d.%m"
TIME_SHORT_FORMAT = r"%H:%M"
DATE_FORMAT = r"%Y-%m-%d"
TIME_FORMAT = r"%H:%M:%S.%f"
DATETIME_FORMAT = f"{DATE_FORMAT} {TIME_FORMAT}"

BABEL_DATE_SHORT_FORMAT = "d MMMM"
BABEL_FULL_WEEK_FORMAT = "EEEE"
BABEL_DATETIME_MEDIUM_FORMAT = "d MMMM Y, HH:mm"


def _format_datetime(
    datetime_: datetime, 
    format: str = BABEL_DATETIME_MEDIUM_FORMAT, 
    locale: str = "ru"
):
    return format_datetime(datetime=datetime_, format=format, locale=locale)


def _format_date(
    date_: date, 
    format: str = BABEL_DATE_SHORT_FORMAT, 
    locale: str = "ru"
):
    return format_date(date=date_, format=format, locale=locale)