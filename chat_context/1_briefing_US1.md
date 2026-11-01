# Briefing for Claude: coach me through US1

Hi Claude. I am Matteo. You have no access to my GitHub repo, so this file gives you the full context. A second file, `2_code_and_level.md`, contains all the current code and my coding level. Please read both before we start.

We will talk by voice. Keep your answers short, one step at a time, and wait for me before you move on.

## 1. Your role

* Act as my coding tutor, not as my ghostwriter.
* Guide me so that I write the code for US1 myself in VS Code.
* Explain each new concept simply: what it is, why we need it here, one tiny example.
* Ask me to type a small piece, run it, and tell you the result. Then continue.
* If I am stuck, give me a hint first. Give the full line only if I ask for it.
* Stay at my level (see file 2). Use only plain Python 3.13, no extra packages, no classes, no advanced tricks.
* At the end of the course I have to explain every line of my code in a Q&A. So I must understand everything we write.
* Use British English. Do not use dash characters in your explanations.

## 2. The project in short

* Course: Programming Foundations, BIT, FHNW, autumn semester 2026, Basel PT, Team B.
* App: "Time Tracker", a console application in Python. Workers log their working days, a manager approves or rejects the entries, both see hour balances. Data is stored in CSV files.
* Team of four. Each person implements three user stories in their own file.
* My file is `timesheet.py`. My stories: US1 log a working day, US5 edit a pending entry, US9 delete a pending entry.
* I also maintain the shared files `main.py` (menus) and `time_logic.py` (rules and calculations). `storage.py` (CSV reading and writing) is maintained by Ahmed.
* Robert has already finished his US4 (filter the timesheet) in `overview.py`. It is a good example of the style the team uses.
* Key dates: complete working app by Wed 2 Dec 2026, hand in on Moodle by Sun 6 Dec 2026, presentation on 9 or 16 Dec.
* The lecturers assess: runs without errors, every promised feature works, and Python foundations (variables, data structures, if / for / while, functions).

## 3. My setup

* Editor: VS Code, with the repo folder opened.
* Run the app from the VS Code terminal in the project folder: `python main.py` (on some Macs `python3 main.py`).
* Login is still a placeholder (Leroy builds the real one): it only asks for the user ID. Use `anna` or `ben` for the worker menu, `carla` for the manager menu.
* Worker menu option `1` calls my function `timesheet.log_working_day(entries, user)`.

## 4. My task: US1, log a working day

As a worker, I want to enter my working day (date, start time, end time, break) so that my hours are recorded correctly and I am paid for what I worked.

Acceptance criteria

1. The worker enters date, start time, end time, break in minutes and an optional comment.
2. `total_hours` = end minus start minus break, shown with two decimals.
3. A valid entry is saved as PENDING. An invalid entry is not saved and the message says which input or rule has to be fixed.

Given, When, Then

1. Given Anna enters 2026-10-14, 08:00, 17:00 and break 60, when she saves, then the entry shows 8.00 h, has status PENDING and is written to `timesheet.csv`.
2. Given start 17:00 and end 08:00, when she saves, then nothing is saved and "end time must be after start time" is shown.
3. Given 08:00 to 16:00 and break 15, when she saves, then nothing is saved and "8.00 h worked needs at least 30 min break" is shown.
4. Edge cases:
   * Date `14.10.2026` or time `8am`: "wrong format", asked again.
   * Break longer than the elapsed time: not saved.
   * More than 10.00 h worked: not saved.
   * A second entry for the same date (same worker): "one entry per day, use edit".

## 5. The rules that apply (from the README)

* Formats: date `YYYY-MM-DD`, time `HH:MM` (24 h), break in whole minutes, hours with two decimals.
* Daily maximum: at most 10.00 h worked per entry, and one entry per worker and date.
* Minimum break (Swiss Labour Act, Art. 15): more than 5.5 h worked needs 15 min, more than 7 h needs 30 min, more than 9 h needs 60 min. A shorter break is rejected and the required break is shown.
* Status values: `PENDING`, `APPROVED`, `REJECTED`. A new entry is always `PENDING`.
* The README says the entry checks should live in `time_logic.py` as functions, because US5 (edit) and Robert's US8 (fix rejected) must use the same checks later.

## 6. What already exists that US1 can use

All of this is in file 2 in full.

* `time_logic.is_valid_date(text)` and `time_logic.is_valid_time(text)`: True or False.
* `time_logic.calculate_total_hours(start_time, end_time, break_minutes)`: returns the worked hours as a float, rounded to two decimals. `break_minutes` must be an int.
* `time_logic.required_break_minutes(worked_hours)`: returns 0, 15, 30 or 60.
* `time_logic.MAX_HOURS_PER_ENTRY` is `10.0`.
* `time_logic.format_hours(8.0)` returns `"8.00 h"`.
* `storage.next_entry_id(entries)`: the next free entry number.
* `entries` is a list of dictionaries, one per row of `timesheet.csv`. Keys: `entry_id, user_id, date, start_time, end_time, break_minutes, total_hours, comment, status, reason`. Values loaded from the CSV are strings.
* `current_user` is a dictionary from `users.csv`, for example `{"user_id": "anna", "name": "Anna Keller", "role": "WORKER", "password": "anna123"}`.
* After my function returns, `main.py` already calls `storage.save_entries(entries)`. So `log_working_day` only needs to append the new dictionary to `entries`. No file code needed in my function.
* Robert's `ask_optional_date(prompt)` in `overview.py` shows the team pattern for "ask again until the input is valid" with `while True`.

## 7. What is still missing (found while reading the code)

* No function checks yet that the end time is after the start time. Careful: `calculate_total_hours("17:00", "08:00", 0)` returns `-9.0` instead of an error, so this check must happen first.
* No check yet that the break is a whole number (for example `"abc"` or `"-5"`), or that the break is not longer than the elapsed time.
* No check yet for more than 10.00 h, the minimum break, or one entry per date.
* `import storage` is not yet at the top of `timesheet.py`.

## 8. Open questions to decide together

1. Where do the checks go? My suggestion: small check functions in `time_logic.py` (which I maintain) so US5 and US8 can reuse them, and the asking and printing in `timesheet.py`.
2. Example 3 says "8.00 h worked", but 08:00 to 16:00 with 15 min break is actually 7.75 h worked (and 7.75 h still needs 30 min). Should the message show 7.75 h? I think yes, and I will tell the team to fix the README.
3. When a rule is broken (end before start, break too short, too many hours): ask everything again, or only go back to the menu? The README only says "not saved" and "the message says what to fix".
4. In the CSV, `total_hours` of old rows looks like `8.0`. Should new rows store `8.0` or `8.00`?

## 9. Suggested plan for our session

1. Walk through `timesheet.py`, `time_logic.py` and the part of `main.py` that calls my function, so I understand what I am building on.
2. Write small "ask until valid" helpers: date, time, break minutes.
3. Write the checks (end after start, break not longer than elapsed, max 10 h, minimum break, one entry per date).
4. Build the new entry dictionary and append it with status `PENDING`.
5. Print a confirmation with the hours, for example `Saved: 2026-10-14, 8.00 h, PENDING`.
6. Add quick `assert` tests under `if __name__ == "__main__":` like Robert did, and test all Given, When, Then examples by hand in the app.
7. Reset the test data afterwards if needed, then commit in VS Code with a clear message.

## 10. Definition of done (team rule)

Acceptance criteria met, runs without errors, I can explain every line, integrated in `main.py` (already done), tested by one teammate, committed with a meaningful message under my own GitHub account.
