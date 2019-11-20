import tkinter as tk
from tkinter import ttk
 
app = tk.Tk() 
app.geometry('200x200')

labelTop = tk.Label(text = "Choose your favourite month")
labelTop.grid(column=5, row=2)

comboExample = ttk.Combobox(
    
                            values=[
                                    "January", 
                                    "February",
                                    "March",
                                    "April"])
print(dict(comboExample)) 
comboExample.grid(column=500, row=500)
comboExample.current(1)

print(comboExample.current(), comboExample.get())

app.mainloop()
