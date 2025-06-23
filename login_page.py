from tkinter import *

root = Tk()
root.title('Login Page')
root.geometry('400x400')

frame = Frame(master=root, height=200, width=360, bg='#d0efff')

label1 = Label(frame, text='Name', bg='#3895D3', fg='white', width=12)
label2 = Label(frame, text='Login ID', bg='#3895D3', fg='white', width=12)
label3 = Label(frame, text='Password', bg='#3895D3', fg='white', width=12)

name = Entry(frame)
email = Entry(frame)
pword = Entry(frame, show='*')

def display():
    name_entry = name.get()
    greet = 'Hey', name_entry
    message = '\nCongratulations your new account has been created'
    textbox.insert(END, greet)
    textbox.insert(END, message)

textbox = Text(bg="#BEBEBE", fg='black')
btn = Button(text='Create Account', command=display, bg='red')

frame.place(x=20, y=0)
label1.place(x=20, y=20)
name.place(x=150, y=20)
label2.place(x=20, y=80)
email.place(x=150, y=80)
label3.place(x=20, y=140)
pword.place(x=150, y=140)
btn.place(x=130, y=210)
textbox.place(y=250)

root.mainloop()