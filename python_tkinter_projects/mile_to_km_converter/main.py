from tkinter import *
MILE_CONVERSION = 1.609

def calculate_converting():
    input_miles = float(user_input.get())
    result = round(input_miles * MILE_CONVERSION,1)
    label_result.config(text=result)

#Window
window = Tk()
window.title("Mile to Km Converter")
window.config(padx=25,pady=25)

#Labels
label_miles = Label(text="Miles")
label_miles.grid(column=2,row=0)

label_km = Label(text="Km")
label_km.grid(column=2,row=1)

label_text = Label(text="is equal to")
label_text.grid(column=0,row=1)

label_result = Label(text=0)
label_result.grid(column=1,row=1)

#Entry
user_input = Entry(width=10)
user_input.insert(END, string="0")
user_input.grid(column=1,row=0)

#Button
button = Button(text="Calculate", command=calculate_converting)
button.grid(column=1,row=2)




window.mainloop()