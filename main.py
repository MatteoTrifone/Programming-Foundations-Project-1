import tkinter
from datetime import datetime

app_window = tkinter.Tk()
app_window.title("Task Tracker")

task_description = tkinter.Label(app_window, text="Task:")
task_description.pack()

task_input = tkinter.Entry(app_window)
task_input.pack()

start_time_label = tkinter.Label(app_window, text="Started: not yet")
start_time_label.pack()


def show_start_time():
    current_time = datetime.now()
    readable_time = current_time.strftime("%H:%M:%S")
    start_time_label.config(text="Started: " + readable_time)


start_button = tkinter.Button(
    app_window,
    text="Start",
    command=show_start_time
)
start_button.pack()

app_window.mainloop()