# Time Tracker

A console application in Python for small companies: workers record their working days, every entry is checked against simple working-time rules, a manager approves or rejects the entries, and both sides see hour balances and reports. Data is stored in CSV files.

Programming Foundations (BIT), FHNW, autumn semester 2026 – Basel PT, Team B.

## Team

| Name | GitHub | Feature area | Own file | User stories |
|---|---|---|---|---|
| Matteo Trifone | MatteoTrifone | Time recording | `timesheet.py` | US1, US5, US9 |
| Robert Nemcsok | robertnemcsok | Worker overview | `overview.py` | US2, US4, US8 |
| Leroy Omokhuale | n9dept | Login and review | `review.py` | US7, US10, US11 |
| Ahmed Holiel | ahmedholiel-rgb | Reports and absences | `reports.py` | US3, US6, US12 |

Each student implements their three user stories in their own file. The shared files (`main.py`, `time_logic.py`, `storage.py`) hold the menu, the common calculations and the CSV access; see [Responsibilities](#responsibilities).

## Revision after the review of 13 October

| Feedback | Where it is answered |
|---|---|
| Console application only | `main.py` is a text menu; the tkinter window was removed. |
| All documentation in one README, Markdown fixed | This file. `ideas.md` and `User Stories.md` were merged into it and deleted. |
| One responsible student per story | [Team](#team), the story headings and [Responsibilities](#responsibilities). |
| US4, US6, US12 were supporting functionality | Replaced: US4 filter the timesheet, US6 monthly overtime summary, US12 absences. Validation, saving and loading are shared work. |
| Given-When-Then with invalid inputs, benefit of US7 | Every story in [User stories](#user-stories). |
| Required hours, balance period, maximum hours, no duplicated warnings | [Working-time rules](#working-time-rules), calculated once in `time_logic.py`. |
| Scope: simple rules, no Excel/PDF export | Excel and PDF export dropped, CSV only. The password login (US7) is kept deliberately small: a user file with a plain-text password, no password change, three attempts. |
| Console interaction, input validation, file processing | [How the app meets the project requirements](#how-the-app-meets-the-project-requirements). |

## Problem statement

Workers and their managers in small companies experience inaccurate and hard-to-check records of working hours in their everyday work, where start and end times are noted on paper or in simple spreadsheets, resulting in wrong hour totals, unclear overtime and extra administrative work for the manager at the end of each month.

## Project goal

Improve the efficiency and effectiveness of time recording: workers enter their working day once, the program calculates the hours and checks the rules immediately, and the manager reviews and sums up the hours without adding up timesheets by hand. Fewer wrong totals, less administrative work, and overtime that everybody can see.

## Scenario

Anna works for a small company. On Tuesday evening she starts the Time Tracker, logs in and enters her day: 2026-10-14, 08:00 to 17:00, 60 minutes break. The program calculates 8.00 hours, checks that the break is long enough and saves the entry as PENDING. On Friday her manager Carla logs in, opens the pending entries, approves Anna's entry and rejects Ben's entry because the break was too short. Ben sees the rejection with the reason, corrects the break and resubmits. At the end of the month Carla opens the team overview and the overtime summary; Anna checks her own balance and sees that she is 6 hours short.

## User roles

| Role | What they do |
|---|---|
| Worker | Logs working days, edits or deletes pending entries, filters the own timesheet, fixes rejected entries, sees the own monthly balance. |
| Manager | Reviews pending entries (approve or reject with a reason), records absences, sees the team overview and the monthly overtime summary. |

## How the app meets the project requirements

| Requirement | How the app meets it |
|---|---|
| Interactive app (user input via the console) | Text menus in `main.py`. After the login a worker menu or a manager menu is shown; every action asks for its values with `input()` and prints the result. |
| Data validation | One set of check functions in `time_logic.py`: date and time format, end after start, break is a whole number that is not longer than the elapsed time, minimum break, daily maximum, one entry per date, known user and password, allowed status and absence type, non-empty rejection reason. Invalid input is never saved and is asked again with a message. |
| File processing | `data/users.csv` is read at start. `data/timesheet.csv` and `data/absences.csv` are read at start and written after every change. A missing timesheet or absence file means an empty start, not an error. |

## Data model and files

All files are CSV files with a header row in the `data` folder.

| File | Fields |
|---|---|
| `users.csv` | `user_id, name, role, password` – role is `WORKER` or `MANAGER` |
| `timesheet.csv` | `entry_id, user_id, date, start_time, end_time, break_minutes, total_hours, comment, status, reason` |
| `absences.csv` | `user_id, date, type` – type is `VACATION`, `SICK` or `HOLIDAY` |

Status values of an entry: `PENDING` (saved, not reviewed), `APPROVED` (counted in reports), `REJECTED` (not counted, `reason` holds the manager's reason).

Formats: date `YYYY-MM-DD`, time `HH:MM` (24 h), break in whole minutes, hours with two decimals, month `YYYY-MM`.

## Working-time rules

Every value is a constant in `time_logic.py`. The balance is calculated by one function that US2 and US6 both call; the entry checks are one set of functions that US1, US5 and US8 call. The surplus warning is shown only in the balance views (US2, US6), never when logging time.

| Rule | Definition |
|---|---|
| Required hours | 8.00 h per working day (Monday to Friday), the same for every worker. Required hours of a month = working days of the month × 8.00 − 8.00 per recorded absence day of that worker (US12). |
| Balance period | One calendar month (`YYYY-MM`). Default is the current month; the user can type another one. |
| Approved hours | Sum of `total_hours` of the worker's APPROVED entries in that month. Pending and rejected entries never count. |
| Balance | approved hours − required hours, shown with a sign and two decimals, e.g. `+3.50 h`. |
| Daily maximum | At most 10.00 h worked per entry and one entry per worker and date. |
| Minimum break | More than 5.5 h worked: 15 min. More than 7 h: 30 min. More than 9 h: 60 min (Swiss Labour Act, Art. 15). A shorter break is rejected and the required break is shown. |
| Surplus warning | A monthly balance above +30.00 h prints one warning line. |

Out of scope: Excel or PDF export, a holiday calendar (public holidays are recorded as absences), password changes or password hashing, night and Sunday work rules.

## User stories

Format: *As a [role], I want to [capability], so that [benefit]*, followed by acceptance criteria and Given-When-Then examples including invalid inputs (Session 02). Names in the examples: workers Anna and Ben, manager Carla.

### Time recording – Matteo (`timesheet.py`)

#### US1 – Log a working day

As a worker, I want to enter my working day (date, start time, end time, break) so that my hours are recorded correctly and I am paid for what I worked.

Acceptance criteria

- The worker enters date, start time, end time, break in minutes and an optional comment.
- `total_hours` = end − start − break, shown with two decimals.
- A valid entry is saved as PENDING. An invalid entry is not saved and the message says which input or rule has to be fixed.

Given-When-Then

- Given Anna enters 2026-10-14, 08:00, 17:00 and break 60, when she saves, then the entry shows 8.00 h, has status PENDING and is written to `timesheet.csv`.
- Given start 17:00 and end 08:00, when she saves, then nothing is saved and "end time must be after start time" is shown.
- Given 08:00 to 16:00 and break 15, when she saves, then nothing is saved and "8.00 h worked needs at least 30 min break" is shown.
- Edge cases: date `14.10.2026` or time `8am` → "wrong format", asked again. Break longer than the elapsed time → not saved. More than 10.00 h worked → not saved. A second entry for the same date → "one entry per day, use edit".

#### US5 – Edit a pending entry

As a worker, I want to edit one of my pending entries so that I can correct a mistake before the manager reviews it.

Acceptance criteria

- Only the worker's own PENDING entries can be selected. Date, start, end, break and comment can be changed.
- The edited entry passes the same checks as a new entry, the hours are calculated again and the status stays PENDING.

Given-When-Then

- Given Anna's pending entry 2026-10-14 08:00–17:00 with break 60, when she changes the end to 18:00, then the entry shows 9.00 h, is still PENDING and the file is updated.
- Given an APPROVED entry, when she tries to edit it, then "approved entries cannot be changed" is shown and nothing changes.
- Edge cases: the new values break a rule (for example break too short) → the old values are kept and the rule is shown. An entry number that is not in her list → "no such entry". Pressing Enter without typing keeps the old value of that field.

#### US9 – Delete a pending entry

As a worker, I want to remove an incorrect pending entry so that my timesheet stays accurate.

Acceptance criteria

- Only the worker's own PENDING entries can be deleted, after a confirmation.
- The entry is removed from the list and from the file.

Given-When-Then

- Given Anna's pending entry no. 3, when she chooses delete and confirms with `y`, then the entry is gone from her timesheet and from `timesheet.csv`.
- Given the same entry, when she answers `n`, then nothing is removed.
- Edge cases: an APPROVED or REJECTED entry → "only pending entries can be deleted". Entry number not in her list → "no such entry". Any answer other than y or n → asked again.

### Worker overview – Robert (`overview.py`)

#### US2 – My monthly balance

As a worker, I want to see my required hours, approved hours and plus/minus balance for a month so that I know whether I am ahead or behind and can correct it.

Acceptance criteria

- Required and approved hours follow the working-time rules; the balance is approved − required.
- Pending hours are listed separately as "not yet counted". A balance above +30.00 h prints a warning line.

Given-When-Then

- Given October 2026 has 22 working days and Anna has 170.00 approved hours, when she opens her balance for 2026-10, then required 176.00, approved 170.00 and balance −6.00 are shown.
- Given Anna also has 2 absence days in October, then required is 160.00 and the balance is +10.00.
- Given a balance of +31.50, then the line "Warning: surplus above +30 h" is printed.
- Edge cases: no approved entries → approved 0.00, balance = −required. Month typed as `10/2026` → "use YYYY-MM". A month in the future → required hours are shown, approved 0.00.

#### US4 – Filter my timesheet

As a worker, I want to filter my timesheet by date range and status so that I can find specific entries quickly.

Acceptance criteria

- Filters: from date, to date (both optional) and status (ALL, PENDING, APPROVED, REJECTED).
- Only the worker's own entries are shown, sorted by date, one row per entry with date, start, end, break, hours and status.

Given-When-Then

- Given Anna has entries on 2026-10-01, 2026-10-08 and 2026-10-15, when she filters from 2026-10-05 to 2026-10-10, then only the entry of 2026-10-08 is listed.
- Given the status filter APPROVED, when she applies it, then only approved entries are listed.
- Edge cases: "from" after "to" → "from date must not be after to date". No matching entry → "no entries found". Unknown status → the four allowed values are listed and asked again. Empty from or to → no limit on that side.

#### US8 – Fix rejected entries

As a worker, I want to see my rejected entries with the manager's reason so that I can correct them and submit them again.

Acceptance criteria

- A list of the worker's REJECTED entries, each with the reason.
- A corrected entry has to pass the entry checks, then goes back to PENDING, the reason is cleared and it appears in the manager's pending list again.

Given-When-Then

- Given Anna's entry of 2026-10-13 was rejected with "break too short", when she opens rejected entries, then the entry and the reason are shown; when she sets the break to 30 and resubmits, then the status is PENDING and Carla sees it under pending entries.
- Given Anna has no rejected entries, then "no rejected entries" is shown.
- Edge cases: the corrected entry still breaks a rule → it stays REJECTED and the rule is shown.

### Login and review – Leroy (`review.py`)

#### US7 – Login

As a member of the organisation, I want to log in with my user ID and password so that only I can see and change my entries and the manager functions stay restricted to managers.

Acceptance criteria

- User ID, role and password come from `users.csv`. Nothing else is shown before the login succeeds.
- Workers get the worker menu, managers the manager menu. Every list and report of a worker is limited to that worker.
- After three failed attempts the program ends.

Given-When-Then

- Given `users.csv` contains anna (WORKER) and carla (MANAGER), when anna enters her correct password, then the worker menu is shown and all lists contain only Anna's entries.
- Given carla enters her correct password, then the manager menu is shown.
- Given a wrong user ID or a wrong password, when the login is checked, then "login failed" is shown without saying which of the two was wrong, and the login is asked again.
- Edge cases: third failed attempt → "too many attempts", the program ends. Empty input → asked again. Missing `users.csv` → a clear error message instead of a crash.

#### US10 – View pending entries

As a manager, I want to see all pending time entries so that I know what needs my review.

Acceptance criteria

- Only PENDING entries of all workers, sorted by date, with a number to select them.
- Columns: no., worker, date, start, end, break, hours, comment.

Given-When-Then

- Given 2 pending, 1 approved and 1 rejected entries, when Carla opens pending entries, then exactly 2 rows are listed with aligned columns.
- Given no pending entries, then "nothing to review" is shown.
- Edge cases: an entry without a comment shows an empty comment column, not `None`.

#### US11 – Approve or reject an entry

As a manager, I want to approve or reject a pending entry, with a reason when rejecting, so that only reviewed time is counted and the worker knows what to fix.

Acceptance criteria

- Choice `a` (approve) or `r` (reject) for a selected pending entry. Rejecting requires a non-empty reason.
- The new status and the reason are saved. Only APPROVED entries count in reports.

Given-When-Then

- Given pending entry no. 2, when Carla chooses `a`, then its status is APPROVED, the file is updated and the hours appear in the team overview.
- Given pending entry no. 2, when Carla chooses `r` and types "break too short", then the status is REJECTED with that reason and Anna sees it under rejected entries.
- Edge cases: empty reason → asked again, the entry stays PENDING. Input other than a or r → asked again. An entry that is no longer pending → "entry is not pending".

### Reports and absences – Ahmed (`reports.py`)

#### US3 – Team overview

As a manager, I want an overview of the approved hours per worker and for the whole team for a month so that I can do the payroll without adding up timesheets by hand.

Acceptance criteria

- One row per worker with the approved hours, then a team total. Only APPROVED entries count.
- A table with aligned columns and hours with two decimals.

Given-When-Then

- Given in October Anna has approved entries of 8.00 and 7.50 h and Ben has 8.00 h approved and 4.00 h pending, when Carla opens the team overview for 2026-10, then Anna 15.50, Ben 8.00 and team total 23.50 are shown.
- Given no approved entries in the month, then every worker shows 0.00 and "no approved hours in this month" is printed.
- Edge cases: month in the wrong format → "use YYYY-MM". A worker with only rejected entries shows 0.00.

#### US6 – Monthly overtime summary

As a manager, I want a monthly overtime summary per worker so that I see who is building up too much overtime or too few hours.

Acceptance criteria

- Per worker: required, approved and balance for the chosen month, then a team balance.
- Workers above +30.00 h are flagged. The balance comes from the same function as in US2.

Given-When-Then

- Given for 2026-10 Anna has required 176.00 and approved 190.00 and Ben has required 176.00 and approved 160.00, when Carla opens the summary, then Anna +14.00, Ben −16.00 and team −2.00 are shown.
- Given Ben's balance is +32.00, then his row is marked with "surplus above +30 h".
- Edge cases: a worker with absence days has reduced required hours. A month without entries → every balance equals −required. Wrong month format → asked again.

#### US12 – Record absences

As a manager, I want to record absences (vacation, sick day, public holiday) for a worker so that required hours and balances are correct on days nobody is expected to work.

Acceptance criteria

- Inputs: worker, date, type (VACATION, SICK, HOLIDAY). Stored in `absences.csv`.
- Each absence day reduces that worker's required hours of its month by 8.00.

Given-When-Then

- Given Carla records anna, 2026-10-16, VACATION, when she saves, then the row is in `absences.csv` and Anna's required hours for October drop from 176.00 to 168.00.
- Given type `party`, when she saves, then it is rejected and the three allowed types are listed.
- Edge cases: a Saturday or Sunday → "absences only on working days". A second absence for the same worker and date → "already recorded". Unknown worker → "unknown user". A date with an existing time entry → "hours were logged on that day".

## Responsibilities

The work is divided by files. Everyone implements their three user stories in their own file and commits under their own GitHub account.

| File | Owner | Content |
|---|---|---|
| `timesheet.py` | Matteo | US1 log a working day, US5 edit, US9 delete |
| `overview.py` | Robert | US2 monthly balance, US4 filter, US8 fix rejected entries |
| `review.py` | Leroy | US7 login, US10 pending entries, US11 approve or reject |
| `reports.py` | Ahmed | US3 team overview, US6 overtime summary, US12 absences |

Shared files are used by everyone and are not counted as user stories. Each has a maintainer who merges changes to it; if you need something in a shared file, write it in the group chat first.

| File | Maintainer | Content |
|---|---|---|
| `main.py` | Matteo | Start, menus, calls the functions of the four feature files |
| `time_logic.py` | Matteo | Constants, worked-hours calculation, entry checks, required hours and balance |
| `storage.py` | Ahmed | Reading and writing the three CSV files |
| `README.md`, `TASKS.md` | everyone | Documentation and task board |

Definition of done for a user story: acceptance criteria met, runs without errors, the owner can explain every line, integrated in `main.py`, tested by one teammate, committed with a meaningful message.

## Program structure and how to run

```text
Programming-Foundations-Project-1/
|-- main.py          start here: login, menus
|-- time_logic.py    constants, calculations, checks (shared)
|-- storage.py       CSV read and write (shared)
|-- timesheet.py     Matteo  US1 US5 US9
|-- overview.py      Robert  US2 US4 US8
|-- review.py        Leroy   US7 US10 US11
|-- reports.py       Ahmed   US3 US6 US12
|-- data/
|   |-- users.csv
|   |-- timesheet.csv
|   `-- absences.csv
|-- README.md
`-- TASKS.md
```

Program flow: start → login (US7) → worker menu or manager menu → chosen action asks for input, calls the calculation and check functions, saves to CSV, prints the result → back to the menu → exit.

Run it with Python 3.13 or newer from the project folder, no extra packages needed:

```bash
python main.py
```

Test users in `data/users.csv`: `anna` and `ben` (workers), `carla` (manager); the passwords are in the file.

## Task board

Who does what and by when: [TASKS.md](TASKS.md).
