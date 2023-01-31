from tkinter import *

window = Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=50, height=50)
window.config(padx=10, pady=10)

input = Entry()
input.grid(column=1, row=0)

miles = Label(text="Miles")
miles.grid(column=2, row=0)

equal = Label(text="is equal to")
equal.grid(column=0, row=1)

kilo_result = Label(text="0")
kilo_result.grid(column=1, row=1)

kilos = Label(text="Km")
kilos.grid(column=2, row=1)

def button_pressed():
    number = float(input.get())
    number *= 1.60934
    kilo_result.config(text=number)

button = Button(text="Calculate", command=(button_pressed))
button.grid(column=1, row=2)

window.mainloop()
