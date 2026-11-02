"""Login and review - Leroy: US7 login, US10 pending entries, US11 approve/reject.

See README for the acceptance criteria and Given-When-Then examples.
"""

import time_logic




def login(users):

    attempts = 0

    while True:
        user_id = input("User ID: ").strip().lower()
        password = input("User Password: ")

        for user in users:
            if user["user_id"].lower() == user_id and user["password"] == password:
                return user

        print("login failed")
        attempts += 1
        if attempts >= 3: 
            print("Too many attempts")
            return None









def show_pending_entries(entries):

    
    for status in entries:
        if status["status"] == "PENDING":
            print(status[1])

    print("US10 - View pending entries: not implemented yet (Leroy)")


def approve_or_reject(entries):
    """US11 - approve (a) or reject (r) with a reason; only pending entries."""
    print("US11 - Approve or reject: not implemented yet (Leroy)")
