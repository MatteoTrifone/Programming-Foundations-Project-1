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
    """Ask until the status is ALL, PENDING, APPROVED or REJECTED."""
    allowed = ["ALL", "PENDING", "APPROVED", "REJECTED"]
    while True:
        status = input("Status (ALL, PENDING, APPROVED, REJECTED): ").strip().upper()
        if status in allowed:
            return status
        print("unknown status, use ALL, PENDING, APPROVED or REJECTED")


def filter_entries(entries, user_id, from_date, to_date, status):
    """Return a new list with only the entries that match all filters.

    from_date and to_date can be "" (no limit), status can be "ALL".
    """
    found = []
    for entry in entries:
        keep = True

        # not my entry -> throw it out
        if entry["user_id"] != user_id:
            keep = False

        # a from date was given and the entry is before it -> throw it out
        if from_date != "" and entry["date"] < from_date:
            keep = False

        # a to date was given and the entry is after it -> throw it out
        if to_date != "" and entry["date"] > to_date:
            keep = False

        # a status was chosen and the entry has another status -> throw it out
        if status != "ALL" and entry["status"] != status:
            keep = False

        if keep == True:
            found.append(entry)
    return found


def sort_by_date(entries):
    """Return a new list with the entries sorted by date (oldest first)."""
    # 1. collect every date once
    dates = []
    for entry in entries:
        if entry["date"] not in dates:
            dates.append(entry["date"])

    # 2. sort the dates (YYYY-MM-DD text sorts in the right order)
    dates = sorted(dates)

    # 3. go through the dates in order and pick the entries of each date
    sorted_entries = []
    for date in dates:
        for entry in entries:
            if entry["date"] == date:
                sorted_entries.append(entry)
    return sorted_entries


def print_entries(entries):
    """Print one row per entry: date, start, end, break, hours, status."""
    for entry in entries:
        date = entry["date"]
        start = entry["start_time"]
        end = entry["end_time"]
        break_minutes = entry["break_minutes"]
        hours = float(entry["total_hours"])
        status = entry["status"]
        print(f"{date}  {start}-{end}  break {break_minutes} min  {hours:.2f} h  {status}")


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

    user_id = current_user["user_id"]
    found = filter_entries(entries, user_id, from_date, to_date, status)

    if len(found) == 0:
        print("no entries found")
        return

    sorted_entries = sort_by_date(found)
    print_entries(sorted_entries)


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

    # Test 1 - README example: from 10-05 to 10-10 -> only Anna's entry of 10-08
    found = filter_entries(test_entries, "anna", "2026-10-05", "2026-10-10", "ALL")
    assert len(found) == 1
    assert found[0]["date"] == "2026-10-08"

    # Test 2 - status filter: only Anna's approved entry, not Ben's
    found = filter_entries(test_entries, "anna", "", "", "APPROVED")
    assert len(found) == 1
    assert found[0]["date"] == "2026-10-01"

    # Test 3 - from and to on the same day: that day is included
    found = filter_entries(test_entries, "anna", "2026-10-08", "2026-10-08", "ALL")
    assert len(found) == 1

    # Test 4 - no limits: all three of Anna's entries
    found = filter_entries(test_entries, "anna", "", "", "ALL")
    assert len(found) == 3

    # Test 5 - nothing found: empty list
    found = filter_entries(test_entries, "anna", "2027-01-01", "", "ALL")
    assert found == []

    # Test 6 - sorting: oldest date first
    found = filter_entries(test_entries, "anna", "", "", "ALL")
    sorted_entries = sort_by_date(found)
    assert sorted_entries[0]["date"] == "2026-10-01"
    assert sorted_entries[1]["date"] == "2026-10-08"
    assert sorted_entries[2]["date"] == "2026-10-15"

    print("all US4 checks passed")
