#User Stories
##1.	As a Worker, I want to log my hours so that I get paid fairly.

## Acceptance criteria 
• The worker manually enters the date, start time, end time and break in CMD.
• Total hours are calculated from the start and end time, minus the break.
• A valid entry is saved as PENDING.
• An optional comment/task can be entered and is saved together with the entry.

##2.	As a Worker, I want an overview of my hours so that I can see my plus/minus hours and correct accordingly.
## Acceptance criteria
• I have a clear view of my required hours and approved hours.
• I can see my plus/minus balance, calculated as approved hours minus required hours.
• A warning is shown if my surplus exceeds +30 hours.

##3.	As a Manager, I want an overview of my workers hours so that I can do the payroll accordingly.
=======

## Acceptance criteria
• A total of worked hours is calculated per worker.
• A team total is calculated.
• Only approved entries are counted.
• The report is readable and consistently formatted.

##4.    As a Manager, I want time entries to pass compliance checks so that working time follows the required rules.

## Acceptance criteria
• Elapsed time is calculated from start and end, and the break is subtracted to get total_hours.
• The date and start/end times must be valid, and the end time must be after the start time.
• The break must be a valid, non-negative duration that does not exceed the elapsed time.
• The break is checked against the legal minimum: 15 minutes for more than 5.5 hours of work, 30 minutes for more than 7 hours, 60 minutes for more than 9 hours (Swiss Labour Act, Art. 15).
• An entry with a break that is too short is not saved, and the worker sees which break is required.
• Maximum working time and surplus rules are checked, including a warning for a surplus over +30 hours.
• Invalid entries are not saved, and the worker sees which input or rule must be corrected.

##5.    As a Worker, I want to be able to change my hours if I made any mistakes in logging them.

## Acceptance criteria
• Only the worker's own PENDING entries can be selected for editing.
• Date, start time, end time, break and the optional comment/task can be changed.
• The worked hours are calculated again and the entry is stored again as PENDING.
• The edited entry must pass the compliance checks before it is saved.
• An entry that is already approved cannot be changed by the worker.

##6.    As a Manager, I want to export approved time data so that I can use it for payroll and reporting.

## Acceptance criteria
• The manager can export approved data to CSV, Excel or PDF.
• Only APPROVED entries are included in the export.
• The export includes the worker, date, start time, end time, break, total hours and optional comment/task.

##7. As an member of the organisation I want to have a secure login protected by a password

## Acceptance criteria
• The user has to enter a user ID and a password before the menu is shown.
• A wrong user ID or password is rejected with a message, and the menu stays locked.
• After login a worker sees only their own entries, and the manager functions are only available to a manager.
• The user's role determines which menu and functions are available after login.

##8. As a Worker, I want to see my rejected entries with the manager's reason so that I can correct them and submit them again.

## Acceptance criteria
• The worker can show only their REJECTED entries.
• Each rejected entry shows the reason the manager gave.
• The worker can correct the rejected entry and resubmit it after it passes the compliance checks.
• After resubmission, its status goes back to PENDING.
• The corrected entry appears again in the manager's list of pending entries.

##9. As a Worker, I want to remove an incorrect pending entry so that my timesheet remains accurate.

## Acceptance criteria
• Only the worker's own PENDING entries can be selected for deletion.
• The worker has to confirm before the entry is removed.
• The entry is removed from the timesheet and from the saved file.
• An entry that is already approved cannot be removed.

##10. As a Manager, I want to see all pending time entries so that I know what requires review.

## Acceptance criteria
• Only PENDING entries are shown.
• Each row shows the worker, date, start time, end time, break, total hours and optional comment/task.
• If there are no pending entries, a clear message is shown.

##11. As a Manager, I want to approve or reject an entry so that only reviewed time is accepted.

## Acceptance criteria
• The manager can choose APPROVED or REJECTED for a selected pending entry.
• The status of the entry changes and is saved.
• The manager stores a reason when an entry is rejected so that the worker can see why it was rejected.
• Only approved entries are counted in the reports.

##12. As a Worker, I want my entries to be saved so that they are still available after restarting the application.

## Acceptance criteria
• Entries are written to a simple CSV file.
• All entries, including their status, rejection reason and optional comment/task, are saved.
• Edits, status changes and deletions are saved to the file and persist after restarting the application.
• Saved entries are loaded again when the application starts.
• If the file does not exist yet, the application starts with an empty timesheet instead of an error.
