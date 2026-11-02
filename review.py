"""Login and review - Leroy: US7 login, US10 pending entries, US11 approve/reject.

See README for the acceptance criteria and Given-When-Then examples.
"""

import time_logic




def login(users):

    attempts = 0

    while True:
        user_id = input("User ID: ").strip().lower()
        password = input("User Password: ")

        for user in users:
            if user["user_id"].lower() == user_id and user["password"] == password:
                return user

        print("login failed")
        attempts += 1
        if attempts >= 3: 
            print("Too many attempts")
            return None




def show_pending_entries(entries):
    # Wir sammeln die offenen Einträge separat, damit wir sie danach
    # sortieren und nummerieren können, ohne die ursprüngliche Liste zu ändern.
    pending = []

    for entry in entries:
        # Jeder Eintrag ist ein Dictionary. Deshalb lesen wir den Status
        # über den Schlüssel "status" aus.
        if entry["status"] == "PENDING":
            pending.append(entry)

    # Das Datumsformat YYYY-MM-DD lässt sich als Text chronologisch sortieren:
    # zum Beispiel steht "2026-10-14" vor "2026-10-15".
    pending.sort(key=lambda entry: entry["date"])

    # Wenn nichts offen ist, gibt es keine Tabelle anzuzeigen.
    # return beendet die Funktion direkt nach dieser Meldung.
    if len(pending) == 0:
        print("nothing to review")
        return

    # Diese Liste legt fest, welche Spalten die Tabelle haben soll.
    headers = [
        "no.", "worker", "date", "start",
        "end", "break", "hours", "comment"
    ]

    # rows enthält die Werte, die später Zeile für Zeile gedruckt werden.
    rows = []

    # enumerate nummeriert die gefilterten Einträge ab 1.
    # So stimmen die Nummern mit der angezeigten Liste überein.
    for number, entry in enumerate(pending, start=1):
        row = [
            str(number),                   # Die Nummer wird als Text gespeichert.
            entry["user_id"],              # Schlüsselzugriff auf die User-ID.
            entry["date"],                 # Datum des Eintrags.
            entry["start_time"],           # Arbeitsbeginn.
            entry["end_time"],             # Arbeitsende.
            str(entry["break_minutes"]),   # In der Tabelle wird Text ausgegeben.
            entry["total_hours"],          # Bereits berechnete Arbeitsstunden.
            entry["comment"] or "",         # None oder leer wird als leerer Text angezeigt.
        ]
        rows.append(row)

    # Wir starten mit der Länge jeder Überschrift als Spaltenbreite.
    # Dadurch passt mindestens die Überschrift in ihre Spalte.
    widths = []

    for column_number in range(len(headers)):
        widest = len(headers[column_number])

        # Wir vergleichen die Überschrift mit allen Zellen dieser Spalte.
        # Die breiteste davon bestimmt die nötige Spaltenbreite.
        for row in rows:
            if len(row[column_number]) > widest:
                widest = len(row[column_number])

        widths.append(widest)

    # ljust füllt jede Überschrift rechts mit Leerzeichen auf.
    # Dadurch beginnen die Werte der nächsten Zeile an derselben Stelle.
    header_line = "  ".join(
        headers[i].ljust(widths[i])
        for i in range(len(headers))
    )
    print(header_line)

    # Dasselbe Ausrichten machen wir für jede Datenzeile.
    # join verbindet die Zellen mit zwei Leerzeichen Abstand.
    for row in rows:
        row_line = "  ".join(
            row[i].ljust(widths[i])
            for i in range(len(row))
        )
        print(row_line)



def approve_or_reject(entries):
    """US11 - approve (a) or reject (r) with a reason; only pending entries."""
    print("US11 - Approve or reject: not implemented yet (Leroy)")
