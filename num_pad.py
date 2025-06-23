from tkinter import *

root = Tk()
root.title('Number pad')
root.geometry('250x300')

frame = Frame(master=root, height=260, width=360, bg="#d0efff")
nums = [['9', '8', '7'], ['6', '5', '4'], ['3', '2', '1'], ['.', '0', '#']]

for i in range(4):
    # configure rows and columns to resize window
    root.columnconfigure(i, weight=1, minsize=75)
    root.rowconfigure(i, weight=1, minsize=50)
    for j in range(0,3):
        frame = Frame(master=root, relief=SUNKEN, borderwidth=1)
        frame.grid(row=i, column=j)
        label = Label(master=frame, text=nums[i][j], bg='#d0efff')
        label.pack(padx=5, pady=5)


root.mainloop()