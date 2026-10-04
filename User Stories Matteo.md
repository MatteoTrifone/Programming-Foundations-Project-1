#User Stories
##1.	As a Worker, I want to log my hours so that I get paid fairly.

## Acceptance criteria 
• A start action records a start time. 
• A stop action records an end time. 
• The two values can be used for later calculation.

##2.	As a Worker, I want an overview of my hours so that I can see my plus/minus hours and correct accordingly.
## Acceptance criteria
• I have a clear view of the worked ours
• I have a clear view of the hours I have to have worked
• I can see how much I'm missing / I'm over

##3.	As a Manager, I want an overview of my workers hours so that I can do the payroll accordingly.
=======

## Acceptance criteria
• A total of worked hours is calculated per worker.
• A team total is calculated.
• Only approved entries are counted.
• The report is readable and consistently formatted.

>>>>>>> 114e762f78aba4200f8f1aa7e8f25727d9f1212b
##4.    As a Manager, I want my workers to have to take brakes according to swiss law.

## Acceptance criteria
• Elapsed time is calculated from start and end, and the break is subtracted to get total_hours.
• The break is checked against the legal minimum: 15 minutes for more than 5.5 hours of work, 30 minutes for more than 7 hours, 60 minutes for more than 9 hours (Swiss Labour Act, Art. 15).
• An entry with a break that is too short is not saved, and the worker sees which break is required.

##5.    As a Worker, I want to be able to change my hours if I made any mistakes in logging them.

## Acceptance criteria
• A pending entry can be selected.
• Start time, end time and break can be changed.
• The worked hours are calculated again and the entry is stored again as PENDING.
• An entry that is already approved cannot be changed by the worker.

##6.    As a Worker, I want to be able to add a comment to my hours that I logged and or changes that I made to add extra information for my manager. 

## Acceptance criteria
• The worker can type a comment when logging or changing an entry. The comment is optional.
• The comment is saved together with the entry.
• The manager sees the comment when reviewing the entry.

##7. As an member of the organisation I want to have a secure login protected by a password

## Acceptance criteria
• The user has to enter a user ID and a password before the menu is shown.
• A wrong user ID or password is rejected with a message, and the menu stays locked.
• After login a worker sees only their own entries, and the manager functions are only available to a manager.

##8. As a Worker, I want to see my rejected entries with the manager's reason so that I can correct them and submit them again.

## Acceptance criteria
• The worker can show only their REJECTED entries.
• Each rejected entry shows the reason the manager gave.
• After the worker corrects the entry, its status goes back to PENDING.
• The corrected entry appears again in the manager's list of pending entries.

##9. As a Worker, I want to remove an incorrect pending entry so that my timesheet remains accurate.

## Acceptance criteria
• A pending entry can be selected.
• The worker has to confirm before the entry is removed.
• The entry is removed from the timesheet and from the saved file.
• An entry that is already approved cannot be removed.

##10. As a Manager, I want to see all pending time entries so that I know what requires review.

## Acceptance criteria
• Only PENDING entries are shown.
• Each row shows the worker, date, start time, end time, break and total hours.
• If there are no pending entries, a clear message is shown.

##11. As a Manager, I want to approve or reject an entry so that only reviewed time is accepted.

## Acceptance criteria
• The manager can choose APPROVED or REJECTED for a selected pending entry.
• The status of the entry changes and is saved.
• A reason can be stored when an entry is rejected.
• Only approved entries are counted in the reports.

##12. As a Worker, I want my entries to be saved so that they are still available after restarting the application.

## Acceptance criteria
• Entries are written to a simple CSV file.
• Saved entries are loaded again when the application starts.
• If the file does not exist yet, the application starts with an empty timesheet instead of an error.
