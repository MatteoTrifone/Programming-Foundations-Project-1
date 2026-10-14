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
