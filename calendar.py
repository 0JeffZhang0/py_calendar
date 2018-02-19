# coding=utf-8
__author__ = 'Leonard'

from turtle import *
import datetime

def write_title(year, month):
    setpos(-350, 250)
    pendown()
    write("{0} {1}".format(get_month_name(month), year), font=('Arial', 20, 'normal'))
    penup()

def write_days():
    xpos = -300
    for day in  ['Sun',  'Mon',  'Tue',  'Wed',  'Thu',  'Fri',  'Sat']:
        setpos(xpos, 200)
        pendown()
        write(day, font=('Arial', 15, 'normal'))
        xpos += 100
        penup()

def draw_regtangle(x, y):
    setpos(x, y)
    pencolor('black')
    pendown()
    for i in range(4):
        forward(100)
        right(90)
    penup()

def draw_graph():
    y = 200
    for raw in range(6):
        x = -350
        for string in range(7):
            draw_regtangle(x, y)
            x += 100
        y -= 100

def draw_date(date, raw, column, today):
    x = column * 100 - 300
    y = raw * -100 + 135
    setpos(x, y)
    if today:
        pencolor('red')
    else:
        pencolor('black')
    pendown()
    write(date, font=('Arial', 15, 'normal'))
    penup()

def draw_dates(year, month, carrent_date):
    raw = 0
    column = get_start_day(year, month)
    for date in range(1, get_num_of_days_in_month(year, month) + 1):
        draw_date(date, raw, column, date == carrent_date)
        column += 1
        if column == 7:
            column = 0
            raw += 1

def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False

def get_num_of_days_in_month(year, month):
    days = 31
    if month in [4, 6, 9, 11]:
        days = 30
    elif month == 2:
        if is_leap_year(year):
            days = 29
        else:
            days = 28
    return days


def get_total_num_of_day(year, month):
    # 自1800年1月1日以来过了多少天
    days = 0
    for y in range(1800, year):
        if is_leap_year(y):
            days += 366
        else:
            days += 365

    for m in range(1, month):
        days += get_num_of_days_in_month(year, m)

    return days


def get_start_day(year, month):
    # 返回当月1日是星期几，由1800.01.01是星期三推算
    return 3 + get_total_num_of_day(year, month) % 7


# 月份与名称对应的字典
month_dict = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June',
              7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}


def get_month_name(month):
    return month_dict[month]



now = datetime.datetime.now()
setup(700, 600)
hideturtle()
tracer(False)
penup()
write_title(now.year, now.month)
write_days()
draw_graph()
draw_dates(now.year, now.month, now.day)
mainloop()