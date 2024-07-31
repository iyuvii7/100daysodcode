from tkinter import *

window = Tk()
window.title("My First GUI program")
window.minsize(height=300, width=500)

# # add label
# my_label = Label(text="I am a label", font=('Arial', 24))
# my_label.config(text="This is new text")
# my_label.pack()
#
#
# def button_clicked():
#     # my_label["text"] = "Button got clicked"
#     my_label.config(text=entry.get())
#
#
# # add button
# my_button = Button(text="Click me", command=button_clicked)
# my_button.pack()
#
# # add entry
# entry = Entry(width=30)
# entry.insert(END, string="Some text to begin")
# entry.pack()
#
# # add text
# text = Text(height=5, width=30)
# # put cursor in textbox
# text.focus()
# text.pack()
# label
label1 = Label(text="Label1")
label1.grid(column=0, row=0)

# button
button = Button(text="Button1")
button.grid(column=1, row=1)

# new button
button1 = Button(text="New Button")
button1.grid(column=2, row=0)

# entry
entry = Entry()
entry.grid(column=3, row=2)


window.mainloop()