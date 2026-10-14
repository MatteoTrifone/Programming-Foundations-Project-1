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
