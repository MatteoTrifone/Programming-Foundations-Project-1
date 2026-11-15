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

    pending = []

    for entry in entries:
        if entry["status"] == "PENDING":
            pending.append(entry)

    pending.sort(key=lambda entry: entry["date"])

    if len(pending) == 0:
        print("nothing to review")
        return

    headers = [
        "no.", "worker", "date", "start",
        "end", "break", "hours", "comment"
    ]

    rows = []

    for number, entry in enumerate(pending, start=1):
        row = [
            str(number),                   # Die Nummer wird als Text gespeichert.
            entry["user_id"],              # Schlüsselzugriff auf die User-ID.
            entry["date"],                 # Datum des Eintrags.
            entry["start_time"],           # Arbeitsbeginn.
            entry["end_time"],             # Arbeitsende.
            str(entry["break_minutes"]),   # In der Tabelle wird Text ausgegeben.
            entry["total_hours"],          # Bereits berechnete Arbeitsstunden.
            entry["comment"] or "",         # None oder leer wird als leerer Text angezeigt.
        ]
        rows.append(row)

    
    widths = []

    for column_numbers in range(len(headers)):
        widest = len(headers[column_numbers])
        
        for row in rows:
            if len(row[column_numbers]) > widest:
                widest = len(row[column_numbers])
        widths.append(widest)

    for i in range(len(headers)):
        if i == len(headers) - 1:
            print(headers[i].ljust(widths[i]))
        else:
            print(headers[i].ljust(widths[i]), end=" | ")

    print("-" * (sum(widths) + 3 * (len(headers) - 1)))

    for row in rows: 
        for i in range(len(row)):
            if i == len(row) - 1:
                print(row[i].ljust(widths[i]))
            else:
                print(row[i].ljust(widths[i]), end= " | ")


def approve_or_reject(entries):

    pending = []

    for entry in entries: 
        if entry["status"] == "PENDING":
            pending.append(entry)

    if len(pending) == 0:
        print("nothing to review")
        return

    pending.sort(key=lambda entry: entry["date"])

    for number, entry in enumerate(pending, start=1):
        print(number, entry["user_id"], entry["date"])

    choice = int(input("Select entry number: "))
    selected_entry = pending[choice - 1]

    
