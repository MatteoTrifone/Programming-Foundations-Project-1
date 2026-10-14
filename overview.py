"""Worker overview - Robert: US2 monthly balance, US4 filter, US8 fix rejected.

Every function gets the shared lists and the logged-in user. Only the
user's own entries are ever shown. US2 uses time_logic.calculate_balance().
See README for the acceptance criteria and Given-When-Then examples.
"""

import time_logic


def show_monthly_balance(entries, absences, current_user):
    """US2 - required, approved and balance for a month, warning above +30 h."""
    print("US2 - My monthly balance: not implemented yet (Robert)")


def filter_timesheet(entries, current_user):
    """US4 - list the user's entries filtered by date range and status."""
    print("US4 - Filter my timesheet: not implemented yet (Robert)")


def fix_rejected_entries(entries, current_user):
    """US8 - show REJECTED entries with the reason, correct and resubmit."""
    print("US8 - Fix rejected entries: not implemented yet (Robert)")
