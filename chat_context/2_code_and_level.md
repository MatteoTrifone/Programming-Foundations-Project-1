# My coding level and the full current code

This is file 2 of 2. File 1 (`1_briefing_US1.md`) explains the project and my task.

## 1. My coding level

Facts:

* I am a first semester student in Programming Foundations (BIT, FHNW, autumn 2026).
* The course assesses these Python foundations: variables, data structures (lists, dictionaries), if / for / while, and functions.
* So far my work in the repo was mostly organisation: problem statement, user stories, README, task board.
* The shared code (`main.py`, `time_logic.py`, `storage.py`) and the empty function skeletons were created on 14 Oct 2026 with the help of an AI assistant. I have not written any feature code myself yet, and I may not understand every line of the shared code.
* US1 is my first own feature.

What this means for you:

* Treat me as a beginner. Explain new things before using them.
* Stick to what the course covers. If you need something beyond that (for example `try` / `except` or `datetime`), explain it in two sentences first.
* Use the patterns already in the code below so my code matches the team style.
* When we use a function from `time_logic.py`, briefly explain how it works, because I will be asked about it.

Fill in during the session (Matteo):

* Things I can already do on my own:
* Things I find hard:

## 2. Python concepts already used in the code below

* Variables, strings, int, float, `round()`
* Lists and dictionaries, a list of dictionaries as the main data structure
* `if` / `elif` / `else`, `for` loops, `while True` with `break` or `return`
* Functions with parameters and `return` values, docstrings
* `input()`, `print()`, f strings with alignment (for example `f"{hours:>8.2f}"`)
* `.strip()`, `.lower()`, `.upper()`, `.startswith()`
* `import` of own modules (`import time_logic`)
* `try` / `except ValueError` and `datetime.strptime` for format checks
* `csv.DictReader` and `csv.DictWriter` (only in `storage.py`)
* `if __name__ == "__main__":` with `assert` quick tests

## 3. Project structure

```text
Programming-Foundations-Project-1/
|-- main.py          start here: login, menus (Matteo maintains)
|-- time_logic.py    constants, calculations, checks (Matteo maintains)
|-- storage.py       CSV read and write (Ahmed maintains)
|-- timesheet.py     Matteo  US1 US5 US9   <- my file
|-- overview.py      Robert  US2 US4 US8   (US4 done)
|-- review.py        Leroy   US7 US10 US11
|-- reports.py       Ahmed   US3 US6 US12
|-- data/
|   |-- users.csv
|   |-- timesheet.csv
|   `-- absences.csv
|-- README.md
`-- TASKS.md
```

## 4. Full code (state of 1 Nov 2026)

### `timesheet.py`

```python
"""Time recording - Matteo: US1 log a working day, US5 edit, US9 delete.

Every function gets the shared lists and the logged-in user and changes the
lists in place. main.py saves the lists to the CSV files afterwards.
See README for the acceptance criteria and Given-When-Then examples.
"""

import time_logic


def log_working_day(entries, current_user):
    """US1 - ask date, start, end, break, comment; check; add as PENDING."""
    print("US1 - Log a working day: not implemented yet (Matteo)")


def edit_pending_entry(entries, current_user):
    """US5 - change one of the user's PENDING entries, re-check, keep PENDING."""
    print("US5 - Edit a pending entry: not implemented yet (Matteo)")


def delete_pending_entry(entries, current_user):
    """US9 - remove one of the user's PENDING entries after a confirmation."""
    print("US9 - Delete a pending entry: not implemented yet (Matteo)")
```

### `time_logic.py`

```python
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
```

### `storage.py`

```python
"""Reading and writing the CSV files (maintainer: Ahmed).

Shared by everyone. Each list holds one dictionary per row, with the
field names of the header row as keys (see README, "Data model and files").
A missing timesheet or absence file means an empty list, not an error.
"""

import csv
import os

DATA_FOLDER = "data"
USERS_FILE = os.path.join(DATA_FOLDER, "users.csv")
TIMESHEET_FILE = os.path.join(DATA_FOLDER, "timesheet.csv")
ABSENCES_FILE = os.path.join(DATA_FOLDER, "absences.csv")

ENTRY_FIELDS = ["entry_id", "user_id", "date", "start_time", "end_time",
                "break_minutes", "total_hours", "comment", "status", "reason"]
ABSENCE_FIELDS = ["user_id", "date", "type"]
USER_FIELDS = ["user_id", "name", "role", "password"]


def read_rows(file_name):
    """All rows of a CSV file as a list of dictionaries. Missing file -> []."""
    if not os.path.exists(file_name):
        return []
    with open(file_name, newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def write_rows(file_name, fields, rows):
    """Write all rows (list of dictionaries) to a CSV file with a header."""
    os.makedirs(DATA_FOLDER, exist_ok=True)
    with open(file_name, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def load_users():
    return read_rows(USERS_FILE)


def load_entries():
    return read_rows(TIMESHEET_FILE)


def save_entries(entries):
    write_rows(TIMESHEET_FILE, ENTRY_FIELDS, entries)


def load_absences():
    return read_rows(ABSENCES_FILE)


def save_absences(absences):
    write_rows(ABSENCES_FILE, ABSENCE_FIELDS, absences)


def next_entry_id(entries):
    """Highest entry_id + 1, or 1 for an empty timesheet."""
    highest = 0
    for entry in entries:
        if int(entry["entry_id"]) > highest:
            highest = int(entry["entry_id"])
    return highest + 1
```

### `main.py`

```python
"""Time Tracker - start here (maintainer: Matteo).

Program flow: load the CSV files -> login (US7) -> worker menu or manager menu
-> the chosen action runs in the owner's file -> the lists are saved -> back
to the menu -> exit. The menu only calls functions; all logic lives in the
feature files (timesheet, overview, review, reports) and in time_logic.
"""

import storage
import timesheet   # Matteo  US1 US5 US9
import overview    # Robert  US2 US4 US8
import review      # Leroy   US7 US10 US11
import reports     # Ahmed   US3 US6 US12

LINE = "=" * 34


def print_menu(title, options):
    """Print a menu box. options is a list of (key, text)."""
    print()
    print(LINE)
    print(f"  TIME TRACKER  -  {title}")
    print(LINE)
    for key, text in options:
        print(f"{key}  {text}")


def worker_menu(entries, absences, user):
    options = [
        ("1", "Log a working day"),
        ("2", "Edit a pending entry"),
        ("3", "Delete a pending entry"),
        ("4", "My timesheet (filter)"),
        ("5", "My monthly balance"),
        ("6", "My rejected entries"),
        ("0", "Exit"),
    ]
    while True:
        print_menu(f"{user['user_id']} (WORKER)", options)
        choice = input("Select: ").strip()
        if choice == "1":
            timesheet.log_working_day(entries, user)
        elif choice == "2":
            timesheet.edit_pending_entry(entries, user)
        elif choice == "3":
            timesheet.delete_pending_entry(entries, user)
        elif choice == "4":
            overview.filter_timesheet(entries, user)
        elif choice == "5":
            overview.show_monthly_balance(entries, absences, user)
        elif choice == "6":
            overview.fix_rejected_entries(entries, user)
        elif choice == "0":
            return
        else:
            print("please choose 0-6")
        storage.save_entries(entries)


def manager_menu(entries, absences, users, user):
    options = [
        ("1", "Pending entries"),
        ("2", "Approve or reject an entry"),
        ("3", "Team overview"),
        ("4", "Monthly overtime summary"),
        ("5", "Record an absence"),
        ("0", "Exit"),
    ]
    while True:
        print_menu(f"{user['user_id']} (MANAGER)", options)
        choice = input("Select: ").strip()
        if choice == "1":
            review.show_pending_entries(entries)
        elif choice == "2":
            review.approve_or_reject(entries)
        elif choice == "3":
            reports.show_team_overview(entries, users)
        elif choice == "4":
            reports.show_overtime_summary(entries, absences, users)
        elif choice == "5":
            reports.record_absence(absences, entries, users)
        elif choice == "0":
            return
        else:
            print("please choose 0-5")
        storage.save_entries(entries)
        storage.save_absences(absences)


def main():
    users = storage.load_users()
    if len(users) == 0:
        print("data/users.csv is missing or empty - cannot start")
        return
    entries = storage.load_entries()
    absences = storage.load_absences()

    print(LINE)
    print("  TIME TRACKER")
    print(LINE)
    user = review.login(users)
    if user is None:
        return
    if user["role"] == "MANAGER":
        manager_menu(entries, absences, users, user)
    else:
        worker_menu(entries, absences, user)
    print("Bye!")


if __name__ == "__main__":
    main()
```

### `overview.py`

```python
"""Worker overview - Robert: US2 monthly balance, US4 filter, US8 fix rejected.

Every function gets the shared lists and the logged-in user. Only the
user's own entries are ever shown. US2 uses time_logic.calculate_balance().
See README for the acceptance criteria and Given-When-Then examples.
"""

import time_logic


def ask_optional_date(prompt):
    """Ask until the input is empty ("" = no limit) or a valid YYYY-MM-DD date."""
    while True:
        text = input(prompt).strip()
        if text == "":
            return ""
        if time_logic.is_valid_date(text):
            return text
        print("wrong format, use YYYY-MM-DD")


def ask_status():
    """Ask until the status filter is ALL, PENDING, APPROVED or REJECTED."""
    while True:
        status = input("Status (ALL, PENDING, APPROVED, REJECTED): ").strip().upper()
        if status == "ALL" or status in time_logic.STATUS_VALUES:
            return status
        print("unknown status, use ALL, PENDING, APPROVED or REJECTED")


def filter_entries(entries, user_id, from_date, to_date, status):
    """Return a new list with the user's entries that match all filters.

    from_date and to_date can be "" (no limit), status can be "ALL".
    No input() and no print() in here, so it can be tested with assert.
    """
    found = []
    for entry in entries:
        same_user = entry["user_id"] == user_id
        after_from = from_date == "" or entry["date"] >= from_date
        before_to = to_date == "" or entry["date"] <= to_date
        same_status = status == "ALL" or entry["status"] == status
        if same_user and after_from and before_to and same_status:
            found.append(entry)
    return found


def sort_by_date(entries):
    """Return a new list with the entries sorted by date (oldest first)."""
    dates = []
    for entry in entries:
        if entry["date"] not in dates:
            dates.append(entry["date"])
    sorted_entries = []
    for day in sorted(dates):
        for entry in entries:
            if entry["date"] == day:
                sorted_entries.append(entry)
    return sorted_entries


def print_entries(entries):
    """Print one aligned row per entry: date, start, end, break, hours, status."""
    print(f"{'Date':<12}{'Start':<7}{'End':<7}{'Break':>6}{'Hours':>8}  Status")
    for entry in entries:
        hours = float(entry["total_hours"])
        line = f"{entry['date']:<12}{entry['start_time']:<7}{entry['end_time']:<7}"
        line = line + f"{entry['break_minutes']:>6}{hours:>8.2f}  {entry['status']}"
        print(line)


def show_monthly_balance(entries, absences, current_user):
    """US2 - required, approved and balance for a month, warning above +30 h."""
    print("US2 - My monthly balance: not implemented yet (Robert)")


def filter_timesheet(entries, current_user):
    """US4 - list the user's entries filtered by date range and status."""
    while True:
        from_date = ask_optional_date("From date (YYYY-MM-DD, Enter = no limit): ")
        to_date = ask_optional_date("To date (YYYY-MM-DD, Enter = no limit): ")
        if from_date != "" and to_date != "" and from_date > to_date:
            print("from date must not be after to date")
        else:
            break
    status = ask_status()
    found = filter_entries(entries, current_user["user_id"], from_date, to_date, status)
    if len(found) == 0:
        print("no entries found")
        return
    print_entries(sort_by_date(found))


def fix_rejected_entries(entries, current_user):
    """US8 - show REJECTED entries with the reason, correct and resubmit."""
    print("US8 - Fix rejected entries: not implemented yet (Robert)")


if __name__ == "__main__":
    # Quick checks for US4: run `python overview.py`
    test_entries = [
        {"user_id": "anna", "date": "2026-10-15", "status": "REJECTED"},
        {"user_id": "anna", "date": "2026-10-01", "status": "APPROVED"},
        {"user_id": "anna", "date": "2026-10-08", "status": "PENDING"},
        {"user_id": "ben", "date": "2026-10-08", "status": "APPROVED"},
    ]

    # README example: from 10-05 to 10-10 -> only Anna's entry of 10-08
    found = filter_entries(test_entries, "anna", "2026-10-05", "2026-10-10", "ALL")
    assert len(found) == 1
    assert found[0]["date"] == "2026-10-08"

    # Status filter: only Anna's approved entry, not Ben's
    found = filter_entries(test_entries, "anna", "", "", "APPROVED")
    assert len(found) == 1
    assert found[0]["date"] == "2026-10-01"

    # Boundary: from and to on the same day includes that day
    found = filter_entries(test_entries, "anna", "2026-10-08", "2026-10-08", "ALL")
    assert len(found) == 1

    # No limits: all three of Anna's entries
    assert len(filter_entries(test_entries, "anna", "", "", "ALL")) == 3

    # Nothing found: empty list
    assert filter_entries(test_entries, "anna", "2027-01-01", "", "ALL") == []

    # Sorting: oldest date first
    ordered = sort_by_date(filter_entries(test_entries, "anna", "", "", "ALL"))
    assert ordered[0]["date"] == "2026-10-01"
    assert ordered[1]["date"] == "2026-10-08"
    assert ordered[2]["date"] == "2026-10-15"

    print("all US4 checks passed")
```

### `review.py`

```python
"""Login and review - Leroy: US7 login, US10 pending entries, US11 approve/reject.

See README for the acceptance criteria and Given-When-Then examples.
"""

import time_logic


def login(users):
    """US7 - ask user ID and password, three attempts, return the user dict.

    TEMPORARY PLACEHOLDER so that main.py runs: asks only the user ID.
    Leroy replaces this with the real login (password check, 'login failed'
    without saying which part was wrong, program ends after 3 attempts).
    """
    while True:
        user_id = input("User ID: ").strip().lower()
        for user in users:
            if user["user_id"].lower() == user_id:
                return user
        print("unknown user, try again")


def show_pending_entries(entries):
    """US10 - numbered list of all PENDING entries, sorted by date."""
    print("US10 - View pending entries: not implemented yet (Leroy)")


def approve_or_reject(entries):
    """US11 - approve (a) or reject (r) with a reason; only pending entries."""
    print("US11 - Approve or reject: not implemented yet (Leroy)")
```

### `reports.py`

```python
"""Reports and absences - Ahmed: US3 team overview, US6 overtime summary, US12 absences.

US3 and US6 only count APPROVED entries. US6 uses time_logic.calculate_balance(),
the same function as US2. US12 changes the absences list in place; main.py saves it.
See README for the acceptance criteria and Given-When-Then examples.
"""

import time_logic


def show_team_overview(entries, users):
    """US3 - approved hours per worker and team total for a month."""
    print("US3 - Team overview: not implemented yet (Ahmed)")


def show_overtime_summary(entries, absences, users):
    """US6 - required, approved, balance per worker for a month; flag > +30 h."""
    print("US6 - Monthly overtime summary: not implemented yet (Ahmed)")


def record_absence(absences, entries, users):
    """US12 - add VACATION / SICK / HOLIDAY for a worker on a working day."""
    print("US12 - Record absences: not implemented yet (Ahmed)")
```

### `data/users.csv`

```text
user_id,name,role,password
anna,Anna Keller,WORKER,anna123
ben,Ben Meier,WORKER,ben123
carla,Carla Frei,MANAGER,carla123
```

### `data/timesheet.csv`

```text
entry_id,user_id,date,start_time,end_time,break_minutes,total_hours,comment,status,reason
1,anna,2026-10-01,08:00,17:00,60,8.0,,APPROVED,
2,anna,2026-10-08,08:00,16:30,30,8.0,,PENDING,
3,anna,2026-10-15,09:00,17:00,15,7.75,,REJECTED,break too short
4,ben,2026-10-08,07:00,15:00,30,7.5,,APPROVED,
```

### `data/absences.csv`

```text
user_id,date,type
```
