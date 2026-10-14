"""Shared constants and calculations (maintainer: Matteo).

Pure functions only: no input(), no print(), no files.
Every rule of the README section "Working-time rules" lives here, so that
US1/US5/US8 (entry checks) and US2/US6 (balance) use the same code.
"""

from datetime import date, datetime

# Working-time rules (see README)
DAILY_HOURS = 8.0            # required hours per working day (Mon-Fri)
MAX_HOURS_PER_ENTRY = 10.0   # more than this is rejected
SURPLUS_WARNING = 30.0       # monthly balance above this prints a warning

# Formats
DATE_FORMAT = "%Y-%m-%d"     # 2026-10-14
TIME_FORMAT = "%H:%M"        # 08:15
MONTH_FORMAT = "%Y-%m"       # 2026-10

# Allowed values
STATUS_VALUES = ["PENDING", "APPROVED", "REJECTED"]
ABSENCE_TYPES = ["VACATION", "SICK", "HOLIDAY"]
ROLES = ["WORKER", "MANAGER"]


def is_valid_date(text):
    """True if text has the form YYYY-MM-DD and is a real date."""
    try:
        datetime.strptime(text, DATE_FORMAT)
        return True
    except ValueError:
        return False


def is_valid_time(text):
    """True if text has the form HH:MM."""
    try:
        datetime.strptime(text, TIME_FORMAT)
        return True
    except ValueError:
        return False


def is_valid_month(text):
    """True if text has the form YYYY-MM."""
    try:
        datetime.strptime(text, MONTH_FORMAT)
        return True
    except ValueError:
        return False


def calculate_total_hours(start_time, end_time, break_minutes):
    """Worked hours = (end - start) - break, rounded to two decimals.

    Example: 08:00, 17:00, 60 -> 8.0
    """
    start = datetime.strptime(start_time, TIME_FORMAT)
    end = datetime.strptime(end_time, TIME_FORMAT)
    elapsed_minutes = (end - start).total_seconds() / 60
    worked_minutes = elapsed_minutes - break_minutes
    return round(worked_minutes / 60, 2)


def required_break_minutes(worked_hours):
    """Minimum break for the worked hours (Swiss Labour Act, Art. 15)."""
    if worked_hours > 9:
        return 60
    if worked_hours > 7:
        return 30
    if worked_hours > 5.5:
        return 15
    return 0


def is_working_day(day):
    """True for Monday to Friday. day is a datetime.date."""
    return day.weekday() < 5


def working_days_in_month(month):
    """Number of Monday-to-Friday days in a month given as YYYY-MM."""
    year = int(month[:4])
    month_number = int(month[5:])
    count = 0
    day_number = 1
    while True:
        try:
            day = date(year, month_number, day_number)
        except ValueError:
            break  # day_number is past the end of the month
        if is_working_day(day):
            count = count + 1
        day_number = day_number + 1
    return count


def required_hours(month, absence_days):
    """Required hours of a month: working days * DAILY_HOURS - absences."""
    return working_days_in_month(month) * DAILY_HOURS - absence_days * DAILY_HOURS


def approved_hours(entries, user_id, month):
    """Sum of total_hours of the user's APPROVED entries in the month."""
    total = 0.0
    for entry in entries:
        same_user = entry["user_id"] == user_id
        same_month = entry["date"].startswith(month)
        if same_user and same_month and entry["status"] == "APPROVED":
            total = total + float(entry["total_hours"])
    return round(total, 2)


def calculate_balance(entries, absences, user_id, month):
    """Balance of one user for one month: approved - required.

    Returns a dictionary with required, approved and balance.
    Used by US2 (own balance) and US6 (overtime summary).
    """
    absence_days = 0
    for absence in absences:
        if absence["user_id"] == user_id and absence["date"].startswith(month):
            absence_days = absence_days + 1
    required = required_hours(month, absence_days)
    approved = approved_hours(entries, user_id, month)
    return {
        "required": round(required, 2),
        "approved": approved,
        "balance": round(approved - required, 2),
    }


def format_hours(hours):
    """8.0 -> '8.00 h'"""
    return f"{hours:.2f} h"


def format_balance(balance):
    """-6.0 -> '-6.00 h', 3.5 -> '+3.50 h'"""
    return f"{balance:+.2f} h"


if __name__ == "__main__":
    # Quick checks: run `python time_logic.py`
    print(calculate_total_hours("08:00", "17:00", 60))   # 8.0
    print(required_break_minutes(8.0))                    # 30
    print(working_days_in_month("2026-10"))               # 22
    print(required_hours("2026-10", 2))                   # 160.0
    print(format_balance(-6.0), format_balance(3.5))      # -6.00 h +3.50 h
