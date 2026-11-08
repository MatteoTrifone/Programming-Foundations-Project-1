"""Reports and absences - Ahmed: US3 team overview, US6 overtime summary, US12 absences.

US3 and US6 only count APPROVED entries. US6 uses time_logic.calculate_balance(),
the same function as US2. US12 changes the absences list in place; main.py saves it.
See README for the acceptance criteria and Given-When-Then examples.
"""

import time_logic


def show_team_overview(entries, users):
    """US3 - approved hours per worker and team total for a month."""
    month = input("Month (YYYY-MM): ")
    if len(month) != 7 or month[4] != "-":
        print("use YYYY-MM")
        return

    team_total = 0.0
    for user in users:
        if user["role"] != "WORKER":
            continue
        total = 0.0
        for entry in entries:
            if (entry["user_id"] == user["user_id"]
                    and entry["status"] == "APPROVED"
                    and entry["date"].startswith(month)):
                total = total + float(entry["total_hours"])
        print(f"{user['name']:<12} {total:>8.2f}")
        team_total = team_total + total

    print(f"{'Team total':<12} {team_total:>8.2f}")
    if team_total == 0:
        print("no approved hours in this month")


def show_overtime_summary(entries, absences, users):
    """US6 - required, approved, balance per worker for a month; flag > +30 h."""
    print("US6 - Monthly overtime summary: not implemented yet (Ahmed)")


def record_absence(absences, entries, users):
    """US12 - add VACATION / SICK / HOLIDAY for a worker on a working day."""
    print("US12 - Record absences: not implemented yet (Ahmed)")
