from tkinter import *

FONT = ("Arial", 14, "bold")

def miles_to_km():
    miles = float(entry.get())
    label_output.config(text=f"{round(miles * 1.60934, 2)}")

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=100, height=100)
window.config(padx=20, pady=20)

entry = Entry(width=12)
entry.insert(END, "0")
entry.grid(column=1, row=0)
label_miles = Label(text="Miles", padx=5, pady=5, font=FONT)
label_miles.grid(column=2, row=0)
is_equal_label = Label(text="is equal to", anchor="e", padx=5, pady=5, font=FONT)
is_equal_label.grid(column=0, row=1)
label_output = Label(text="0", padx=5, pady=5, font=FONT)
label_output.grid(column=1, row=1)
label_km = Label(text="Km", padx=5, pady=5, font=FONT)
label_km.grid(column=2, row=1)

button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)



window.mainloop()


