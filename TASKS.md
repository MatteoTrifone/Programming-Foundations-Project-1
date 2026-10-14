# Task board

Who does what, and by when. Team B: Matteo, Robert, Leroy, Ahmed.

**How to tick a box:** open this file on GitHub, click the pencil (Edit), change `[ ]` to `[x]` on your line, then click "Commit changes". In VS Code: pull, edit the same way, commit, push. Tick only your own lines, and the **Team** lines once the whole team agrees they are done.

**Who owns what** (details in [README.md](README.md)): everyone works in their own file.

| Owner | File | User stories |
|---|---|---|
| Matteo | `timesheet.py` | US1 log a working day, US5 edit, US9 delete |
| Robert | `overview.py` | US2 monthly balance, US4 filter, US8 fix rejected entries |
| Leroy | `review.py` | US7 login, US10 pending entries, US11 approve or reject |
| Ahmed | `reports.py` | US3 team overview, US6 overtime summary, US12 absences |

Shared files: `main.py` and `time_logic.py` (Matteo maintains), `storage.py` (Ahmed maintains). Ask in the group chat before changing a shared file.

## Deadlines at a glance

| When | What |
|---|---|
| Wed 7 Oct, 13:15 | User stories ready for class, scope agreed with the lecturers |
| Sun 11 Oct | User stories defined (CW 41): in the repo and uploaded to Moodle |
| Wed 21 Oct | Program flow defined and core functions implemented (CW 43) |
| Wed 2 Dec | Complete, working application (CW 49, project coaching in class) |
| **Sun 6 Dec, 23:55** | **Hand in on Moodle.** Up to 72 hours late: grade capped at 4.0. Later: 1.0 |
| Wed 9 or 16 Dec | Final presentation, 15 minutes plus Q&A (slot not announced yet) |

The dates in this table come from the semester programme and the project guidelines. Other dates below are our own targets to stay on track.

## This week: CW 42 (12 – 18 Oct): answer Phillip's feedback

Phillip reviewed the repo on 13 Oct and did not approve it yet. The README was rewritten on 14 Oct to answer his points (one README, console app, owners, three new stories, Given-When-Then, working-time rules, project requirements).

- [x] **Matteo**: read your three stories (US1, US5, US9) in the README and correct what you would build differently
- [x] **Robert**: read your three stories (US2, US4, US8) in the README and correct what you would build differently
- [x] **Leroy**: read your three stories (US7, US10, US11) in the README and correct what you would build differently
- [x] **Ahmed**: read your three stories (US3, US6, US12) in the README and correct what you would build differently
- [ ] **Robert**: reply to Phillip with the repo link once everyone has checked their stories (target Fri 17 Oct)
- [ ] **Team**: split every user story into tasks, each with an owner

## CW 43 (19 – 25 Oct): milestone on Wed 21 Oct

Program flow and shared functions are already in `main.py`, `time_logic.py` and `storage.py`. Each owner now fills the functions in their own file.

- [ ] **Team**: walk through the program flow in `main.py` together (login, menus, save) and fix what is unclear
- [ ] **Team**: agree that the entry fields and status values in the README are final
- [ ] **Matteo**: US1 log a working day works end to end (input, checks, PENDING, saved to CSV)
- [ ] **Robert**: US4 filter my timesheet works (list the own entries by date range and status)
- [ ] **Leroy**: US7 login works (password check, three attempts) and replaces the placeholder
- [ ] **Ahmed**: US3 team overview works (approved hours per worker, team total)

## CW 44 – 48 (26 Oct – 29 Nov): build

No class in CW 45 (2 – 8 Nov). Each member implements their own 3 user stories in their own file and commits them under their own GitHub account. Target: Wed 2 Dec.

- [ ] **Matteo**: US5 edit a pending entry and US9 delete a pending entry done
- [ ] **Robert**: US2 monthly balance and US8 fix rejected entries done
- [ ] **Leroy**: US10 pending entries and US11 approve or reject done
- [ ] **Ahmed**: US6 monthly overtime summary and US12 record absences done
- [ ] **Everyone**: one teammate has tested each of your stories against the Given-When-Then examples

## CW 49 (30 Nov – 6 Dec): finish and hand in

### By Wed 2 Dec

- [ ] **Team**: complete, working application (bring open questions to the coaching session)
- [ ] **Team**: check functionality against the assessment sheet (30 points): runs without errors, every promised feature works
- [ ] **Team**: check the Python foundations against the assessment sheet (30 points): variables, data structures, if / for / while, functions

### By Sun 6 Dec, 23:55

- [ ] **Team**: every section of the README.md template filled in (main functionality, project structure, how to run it)
- [ ] **Team**: each member's contribution stated in the documentation
- [ ] **Team**: slides for the 15-minute presentation (why this topic, goals and features, project management, live demo)
- [ ] **Team**: repository set to public (test the link in a private browser window)
- [ ] **Team**: slides exported as PDF with the link to this repository in them
- [ ] **Team**: handed in on Moodle (presentation PDF and Declaration of Originality)

## CW 50 – 51 (7 – 20 Dec): presentation

- [ ] **Everyone**: be ready to explain every line of your code. The Q&A has individual questions on your own user stories
- [ ] **Team**: final presentation, Wed 9 or 16 Dec

## Done

- [x] **Team**: group registered on Moodle (Basel PT, Team B)
- [x] **Team**: team repo created and everyone invited
- [x] **Team**: problem statement and project goal written (now in README.md)
- [x] **Everyone**: user stories written (CW 41)
- [x] **Team**: topic and user stories discussed with the lecturers in class, Wed 7 Oct
- [x] **Team**: repo link uploaded to Moodle (7 Oct)
- [x] **Team**: tkinter window replaced by a console menu (14 Oct)
- [x] **Matteo**: README rewritten after Phillip's feedback (14 Oct)
