from tkinter import *
from tkinter.font import Font
import calendar
year = 2020

def yearDecrease(yearEntry):
    global year
    y = int(year)
    y -= 1
    year = y
    yearEntry.delete(0, END)
    yearEntry.insert(0, y)

def yearIncrease(yearEntry):
    global year
    y = int(year)
    y += 1
    year = y
    yearEntry.delete(0, END)
    yearEntry.insert(0, y)

def getCalendar(yearEntry, cal_year):
    global year
    year = int(yearEntry.get())
    myCalendar = calendar.calendar(year)
    cal_year.config(text = myCalendar)

if __name__ == '__main__':
    root = Tk()
    root.title("Calendar")
    root.geometry("550x750")
    root.resizable(0, 0)

    my_font = Font(family="Ethnocentric Rg", size=20)
    WelcomeMsg = Label(root, text = "Desktop Calendar", font = my_font )
    WelcomeMsg.pack(ipadx = 30, ipady = 6)

    yearEntry = Entry(root, justify = "center", font="Consolas 10 bold")
    yearEntry.insert(0,year)
    yearEntry.pack(ipadx = 30, ipady = 3)

    Lbutton = Button(root, text = '<', padx=1,pady=1, font=('Cambria',10,'bold'), command=lambda: yearDecrease(yearEntry))
    Lbutton.place(x=155 , y=50)
    Rbutton = Button(root, text='>', padx=1, pady=1, font=('Cambria', 10, 'bold'), command=lambda: yearIncrease(yearEntry))
    Rbutton.place(x=365, y=50)

    button = Button(root, text="Ok!", padx=1, pady=1, font=('Cambria', 10, 'bold'), command=lambda: getCalendar(yearEntry, cal_year))
    button.pack()

    myCalendar = calendar.calendar(year)
    cal_year = Label(root, text=myCalendar, font="Consolas 10 bold", justify = LEFT)
    cal_year.pack()

    root.mainloop()