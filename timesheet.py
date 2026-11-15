"""Time recording - Matteo: US1 log a working day, US5 edit, US9 delete.

Every function gets the shared lists and the logged-in user and changes the
lists in place. main.py saves the lists to the CSV files afterwards.
See README for the acceptance criteria and Given-When-Then examples.
"""

import time_logic
import storage

LINE_TIMESHEET = "=" * 34

def ask_date(old_date=""):
    while True:
        print(LINE_TIMESHEET)
        print("Please use format: YYYY-MM-DD")
        print(LINE_TIMESHEET)
        if old_date != "":
            print(f"Current date: {old_date} (press Enter to keep)")
        input_date = input("For which day? ").strip()

        if input_date == "" and old_date != "":
            return old_date
        
        if time_logic.is_valid_date(input_date):
            return input_date
        else: 
            print("Please input a valid date format.")

def ask_start_time(old_start_time=""):
    while True:
        print(LINE_TIMESHEET)
        print("Please use format: HH:MM")
        print(LINE_TIMESHEET)
        if old_start_time != "":
            print(f"Current start time: {old_start_time} (press Enter to keep)")
        input_time = input("When did you start working? ").strip()

        if input_time == "" and old_start_time != "":
            return old_start_time

        if time_logic.is_valid_time(input_time):
            return input_time
        else: 
            print("Please input a valid time format.")

def ask_end_time(old_end_time=""):
    while True:
        print(LINE_TIMESHEET)
        if old_end_time != "":
            print(f"Current end time: {old_end_time} (press Enter to keep)")
        input_time = input("When did you finish working? ").strip()

        if input_time == "" and old_end_time != "":
            return old_end_time

        if time_logic.is_valid_time(input_time):
            return input_time
        else: 
            print("Please input a valid time format.")

def ask_break(old_break=""):
    while True:
        print(LINE_TIMESHEET)
        print("Please write how many whole minutes.")
        print(LINE_TIMESHEET)
        if old_break != "":
            print(f"Current break: {old_break} min (press Enter to keep)")
        input_break = input("How long was your break? ").strip()

        if input_break == "" and old_break != "":
            return int(old_break)

        if input_break.isdecimal():
            return int(input_break)
        else:
            print("e.g. 30")

def ask_comment(old_comment=""):

    if old_comment == "":
        while True:
            is_there_a_comment = input("Would you like to add a comment? (y/n) ").strip().lower()        
            if is_there_a_comment == "y": 
                comment = input("Comment: ").strip()
                print(LINE_TIMESHEET)
                return comment
            elif is_there_a_comment == "n" or is_there_a_comment == "":
                print("Thank you and have a nice day")
                return ""
            else: print("Please input either y or n.")
    else:
        while True:
            is_there_a_comment = input("Would you like to change the comment? (y/n) ").strip().lower()        
            if is_there_a_comment == "y": 
                comment = input("New comment: ").strip()
                print(LINE_TIMESHEET)
                return comment
            elif is_there_a_comment == "n" or is_there_a_comment == "":
                print("Thank you and have a nice day")
                return old_comment
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

    message = time_logic.check_full_entry(date,start_time,end_time,break_length,entries,current_user["user_id"],0)

    if message != "":
        print(message)
        return

    entry_id = storage.next_entry_id(entries)

    worked_hours = time_logic.calculate_total_hours(start_time,end_time,break_length)

    entries.append({"entry_id": entry_id,"user_id":current_user["user_id"],"date":date,"start_time":start_time,"end_time":end_time,"break_minutes":break_length,"total_hours":worked_hours,"comment":comment,"status":status,"reason":reason})

def show_entries(entries,current_user):
    """Creates a list with all the entries for one user, shows them and returns it."""
    single_user_entries = []
    
    for entry in entries: 
        if entry["user_id"] == current_user["user_id"]:
            single_user_entries.append(entry)

    if len(single_user_entries) == 0:
        print("Error, no entries found.")
        return single_user_entries
    
    for entry_number, entry in enumerate(single_user_entries,start = 1):
                date = entry["date"]
                start = entry["start_time"]
                end = entry["end_time"]
                break_minutes = entry["break_minutes"]
                hours = float(entry["total_hours"])
                comment = entry["comment"]
                status = entry["status"]
                print(f"{entry_number}  {date}  {start}-{end}  break {break_minutes} min  {hours:.2f} h  comment  {comment}  {status}")
    return(single_user_entries)

def choose_single_user_entries(single_user_entries):
    """Requests input from user and validates that input as a selection of the chosen entry and returns either the selection or 0 if cancelled."""
    while True:

        chosen_entry = input(f"{LINE_TIMESHEET}\nInput 0 to cancel\nWhich entry do you choose? ").strip()

        if chosen_entry.isdecimal() == False:
            print("Please input a valid number")
            continue
        
        chosen_entry = int(chosen_entry)

        if chosen_entry == 0:
            return 0

        if chosen_entry > len(single_user_entries):
            print("No such entry found.")
            continue       
        return (single_user_entries[chosen_entry - 1])

def show_single_entry(entry):
    """Prints a whole entry that is given in the parameter."""
    date = entry["date"]
    start = entry["start_time"]
    end = entry["end_time"]
    break_minutes = entry["break_minutes"]
    hours = float(entry["total_hours"])
    comment = entry["comment"]
    status = entry["status"]
    print(f"{date}  {start}-{end}  break {break_minutes} min  {hours:.2f} h  comment  {comment}  {status}")

def edit_pending_entry(entries, current_user):
    """US5 - change one of the user's PENDING entries, re-check, keep PENDING."""
    while True:    
        single_user_entries = show_entries(entries,current_user)

        if len(single_user_entries) == 0:
            return

        chosen_entry = choose_single_user_entries(single_user_entries)    

        if chosen_entry == 0:
            return
        if chosen_entry["status"] == "APPROVED":
            print("Error, approved entries cannot be changed.")
            continue
        if chosen_entry["status"] == "REJECTED":
            print("Error, rejected entries can be changed under option 6 in the main menu.")
            continue
        break    

    new_date = ask_date(chosen_entry["date"])

    new_start_time = ask_start_time(chosen_entry["start_time"])

    new_end_time = ask_end_time(chosen_entry["end_time"])

    new_break = ask_break(chosen_entry["break_minutes"])

    print(f"Current comment: {chosen_entry["comment"]}")
    new_comment = ask_comment(chosen_entry["comment"])

    message = time_logic.check_full_entry(new_date,new_start_time,new_end_time,new_break,entries,current_user["user_id"],chosen_entry["entry_id"])

    if message != "":
        print(message)
        return
    print("Old entry:")
    show_single_entry(chosen_entry)

    print("New entry:")
    worked_hours = time_logic.calculate_total_hours(new_start_time,new_end_time,new_break)
    temporary_entry = {"date":new_date,"start_time":new_start_time,"end_time":new_end_time,"break_minutes":new_break,"total_hours":worked_hours,"comment":new_comment,"status":"PENDING"}
    show_single_entry(temporary_entry)

    while True:
        entry_change_confirmed = input("Would you like to save changes? (y/n) ").strip().lower()  

        if entry_change_confirmed == "y":
            chosen_entry.update(temporary_entry)
            print("Entry successfully updated.")
            return
        
        elif entry_change_confirmed == "n":
            print("New entry was not saved.")
            return
        
        else: print("Please input either y or n.")

def delete_pending_entry(entries, current_user):
    """US9 - remove one of the user's PENDING entries after a confirmation."""
    print("US9 - Delete a pending entry: not implemented yet (Matteo)")