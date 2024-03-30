from tkinter import *

# Create window with title and size
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=350, height=100)

# text for is equal to
equal_text = Label(text="is equal to")
equal_text.grid(column=0, row=1)

# miles text after entry box
miles_text = Label(text="Miles")
miles_text.grid(column=2, row=0)

# km text
Km_text = Label(text="Km")
Km_text.grid(column=2, row=1)

# input miles
input_miles = Entry(width=5)
input_miles.grid(column=1, row=0)

# converted km value
km_value = Label()
km_value.grid(column=1, row=1)

# FCN to calc m to km
def calculate_km():
    value = int(input_miles.get())
    km = value / 1000
    km_value["text"] = km

# button to convert m to km and display it in km label
calculate_button = Button(text="Calculate", command=calculate_km)
calculate_button.grid(column=1, row=2)












window.mainloop()