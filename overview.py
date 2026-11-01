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
