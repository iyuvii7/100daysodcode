from tkinter import *

window = Tk()
window.title("Mile to KM Converter")
window.minsize(height=150, width=150)

label1 = Label(text="is equal to")
label1.grid(column=0, row=1)

entry = Entry()
entry.grid(column=1, row=0)

label2 = Label(text="Miles")
label2.grid(column=2, row=0)

label3 = Label(text="KM")
label3.grid(column=2, row=1)

label4 = Label()
label4.grid(column=1, row=1)


def mile_to_km():
    mile = int(entry.get())
    result = mile * 1.609344
    label4.config(text=result)

button = Button(command=mile_to_km, text="Calculate")
button.grid(column=1, row=2)



window.mainloop()
