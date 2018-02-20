import datetime
from tkinter import *
from tkinter.ttk import Combobox

import calendar

action_date = {}


def draw_days():
    column = 0
    for day in ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']:
        Label(win, text=day, width=13).grid(column=column, row=2)
        column += 1


def draw_dates():
    for widget in body_frame.winfo_children():
        widget.destroy()
    row = 0
    column = calendar.get_start_day(year.get(), month.get())
    if column >= 7:
        column -= 7
    now = datetime.datetime.now()
    for date in range(1, calendar.get_num_of_days_in_month(year.get(), month.get()) + 1):
        if year.get() == now.year and month.get() == now.month and date == now.day:
            text_color = 'red'
        else:
            text_color = 'black'
        Label(body_frame, text=date, width=13, borderwidth=1, relief='solid', fg=text_color).grid(column=column, row=row)
        column += 1
        if column == 7:
            column = 0
            row += 1


def go_to_today():
    now = datetime.datetime.now()
    action_date['year'] = year
    year.set(now.year)
    action_date['month'] = month
    month.set(now.month)
    action_date['day'] = now.day


def click_today():
    go_to_today()
    draw_dates()


def month_change(event):
    draw_dates()


win = Tk()
win.title("Python calendar")
today_button = Button(win, text="Today", command=click_today)
today_button.grid(column=2, row=1)

year = IntVar()
year_edit = Entry(win, width=12, textvariable=year)
year_edit.bind("<Return>", month_change)
year_edit.grid(column=0, row=1)
year_edit.focus()

body_frame = Frame(win)
body_frame.grid(row=3, column=0, columnspan=7)

month = IntVar()
month_list = Combobox(win, width=12, textvariable=month)
month_list.bind("<<ComboboxSelected>>", month_change)
month_list['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
month_list.grid(column=1, row=1)
month_list.current(0)
draw_days()
draw_dates()
click_today()

win.mainloop()