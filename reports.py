"""Reports and absences - Ahmed: US3 team overview, US6 overtime summary, US12 absences.

US3 and US6 only count APPROVED entries. US6 uses time_logic.calculate_balance(),
the same function as US2. US12 changes the absences list in place; main.py saves it.
See README for the acceptance criteria and Given-When-Then examples.
"""

import time_logic


def show_team_overview(entries, users):
    """US3 - approved hours per worker and team total for a month."""
    print("US3 - Team overview: not implemented yet (Ahmed)")


def show_overtime_summary(entries, absences, users):
    """US6 - required, approved, balance per worker for a month; flag > +30 h."""
    print("US6 - Monthly overtime summary: not implemented yet (Ahmed)")


def record_absence(absences, entries, users):
    """US12 - add VACATION / SICK / HOLIDAY for a worker on a working day."""
    print("US12 - Record absences: not implemented yet (Ahmed)")
