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
