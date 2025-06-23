from tkinter import *
from datetime import date

root = Tk()
root.title('Age Calculator App')
root.geometry('400x400')

frame = Frame(master=root, height=250, width=360, bg='#d0efff')

label1 = Label(frame, text='Name', bg = "#3895D3", fg = 'white', width = 12)
label2 = Label(frame, text='Date', bg='#3895D3', fg='white', width=12)
label3 = Label(frame, text='Month', bg='#3895D3', fg='white', width=12)
label4 = Label(frame, text='Year', bg='#3895D3', fg='white', width=12)

name = Entry(frame)
day = Entry(frame)
month = Entry(frame)
year = Entry(frame)

def display():
    n = name.get()
    d = int(day.get())
    m = int(month.get())
    y = int(year.get())
    today = date.today()
    # Calculate Age
    age = today.year - y -((today.month, today.day)<(m,d))
    result.config(text=f"{n}'s age is {age}")

result = Label()
btn = Button(text='Calculate Age', command=display, fg='#065C96')

frame.place(x=20, y=0)
label1.place(x=20, y=20)
name.place(x=150, y=20)
label2.place(x=20, y=80)
day.place(x=150, y=80)
label3.place(x=20, y=140)
month.place(x=150, y=140)
label4.place(x=20, y=200)
year.place(x=150, y=200)
btn.place(x=130, y=250)
result.place(x=20, y=270)
root.mainloop()


