from tkinter import *
from datetime import datetime

app = Tk()
app.title('Age Calculator')
app.geometry('250x250')

msg = Label(app, text='Enter your DOB')
msg.grid(row=0, column=0, columnspan=3)

dayL = Label(app, text='Day: ')
dayE = Entry(app, width=2)

monL = Label(app, text='Month: ')
monE = Entry(app, width=2)

yrL = Label(app, text='Year: ')
yrE = Entry(app, width=4)

dayL.grid(row=1, column=0)
dayE.grid(row=1, column=1)
monL.grid(row=1, column=2)
monE.grid(row=1, column=3)
yrL.grid(row=1, column=4)
yrE.grid(row=1, column=5)


def findDays():
    date = int(dayE.get())
    mon = int(monE.get())
    year = int(yrE.get())
    dob = datetime(day=date, month=mon, year=year)

    time_now = datetime.now()
    time_dif = time_now - dob

    dys = Label(app, text='You Lived ' + str(time_dif.days) + ' days')
    dys.grid(row=3, columnspan=4, column=0)


def findSec():
    date = eval(dayE.get())
    mon = int(monE.get())
    year = int(yrE.get())
    dob = datetime(day=date, month=mon, year=year)

    time_now = datetime.now()
    time_dif = time_now - dob

    dys = Label(app, text='You Lived ' + str(time_dif.total_seconds()) + ' seconds')
    dys.grid(row=4, columnspan=6, column=0)


dysB = Button(app, text='Total Days', command=findDays)
dysB.grid(row=2,column=0,columnspan=3)
dysS = Button(app, text='Total Seconds', command=findSec)
dysS.grid(row=2,column=3,columnspan=3)
app.mainloop()
