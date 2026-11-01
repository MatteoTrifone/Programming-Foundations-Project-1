"""Time recording - Matteo: US1 log a working day, US5 edit, US9 delete.

Every function gets the shared lists and the logged-in user and changes the
lists in place. main.py saves the lists to the CSV files afterwards.
See README for the acceptance criteria and Given-When-Then examples.
"""

import time_logic
import storage

LINE_TIMESHEET = "=" * 34

def ask_date():
    while True:
        print(LINE_TIMESHEET)
        print("Please use format: YYYY-MM-DD")
        print(LINE_TIMESHEET)
        input_date = input("For which day? ").strip()
        
        if time_logic.is_valid_date(input_date):
            return input_date
        else: 
            print("Please input a valid date format.")

def ask_start_time():
    while True:
        print(LINE_TIMESHEET)
        print("Please use format: HH:MM")
        print(LINE_TIMESHEET)
        input_time = input("When did you start working? ").strip()
        if time_logic.is_valid_time(input_time):
            return input_time
        else: 
            print("Please input a valid time format.")

def ask_end_time():
    while True:
        print(LINE_TIMESHEET)
        input_time = input("When did you finish working? ").strip()
        if time_logic.is_valid_time(input_time):
            return input_time
        else: 
            print("Please input a valid time format.")

def ask_break():
    while True:
        print(LINE_TIMESHEET)
        print("Please write how many whole minutes.")
        print(LINE_TIMESHEET)
        input_break = input("How long was your break? ").strip()
        if input_break.isdigit():
            return int(input_break)
        else:
            print("e.g. 30")

def ask_comment():
    while True:
        is_there_a_comment = input("Would you like to add a comment? (y/n) ").strip().lower()
        if is_there_a_comment == "y": 
            comment = input("Comment: ").strip()
            print(LINE_TIMESHEET)
            return comment
        elif is_there_a_comment == "n":
            print("Thank you and have a nice day")
            return ""
        else: print("Please input either y or n.")

def log_working_day(entries, current_user):
    """US1 - ask date, start, end, break, comment; check; add as PENDING."""
    date = ask_date()
    start_time = ask_start_time()
    end_time = ask_end_time()
    break_length = ask_break()
    comment = ask_comment()
    status = "PENDING"
    reason = ""
    print(LINE_TIMESHEET)
    print(f"Date: {date}")
    print(f"Start: {start_time}")
    print(f"End: {end_time}")
    print(f"Break: {break_length}")
    print(f"Comment: {comment}")
    print(LINE_TIMESHEET)

    if end_time <= start_time:
        print(LINE_TIMESHEET)
        print("Start time must be before end time")
        return
    
    worked_hours = time_logic.calculate_total_hours(start_time,end_time,break_length)
    if worked_hours <= 0:
        print(LINE_TIMESHEET)
        print("Error. Worked hours can't be 0 or less than 0.")
        return
    
    if worked_hours > 10:
        print(LINE_TIMESHEET)
        print("Error. Worked hours can't be more than 10.")
        return
    
    for entry in entries:
        if current_user["user_id"] == entry["user_id"] and date == entry["date"]:
            print(LINE_TIMESHEET)
            print("Please input one entry per date.")
            return

    if time_logic.required_break_minutes(worked_hours) >= break_length:
        print(LINE_TIMESHEET)
        print("Please input valid break length.") 
        print("Break length too short.")       
        return
    
    entry_id = storage.next_entry_id(entries)

    entries.append({"entry_id": entry_id,"user_id":current_user["user_id"],"date":date,"start_time":start_time,"end_time":end_time,"break_minutes":break_length,"total_hours":worked_hours,"comment":comment,"status":status,"reason":reason})


def edit_pending_entry(entries, current_user):
    """US5 - change one of the user's PENDING entries, re-check, keep PENDING."""
    print("US5 - Edit a pending entry: not implemented yet (Matteo)")


def delete_pending_entry(entries, current_user):
    """US9 - remove one of the user's PENDING entries after a confirmation."""
    print("US9 - Delete a pending entry: not implemented yet (Matteo)")