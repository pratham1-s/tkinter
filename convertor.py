# -*- coding: utf-8 -*-
"""
Created on Mon May 15 21:25:07 2023

@author: sharma
"""

from tkinter import *

def convert():
    val_changed = int(entry.get())*1.60934
    val_label.config(text=str(val_changed))
    
window = Tk()
window.title('Miles to KM convertor')
window.minsize(width=500, height=500)

entry = Entry(width=20)
entry.grid(row=0, column=1)

miles_label = Label(text='Miles', font=('Arial', 24, 'bold'))
miles_label.grid(row=0, column=2)

equal_label = Label(text='is equal to', font=('Arial', 24, 'bold'))
equal_label.grid(row=1, column=0)

val_label = Label(text='0', font=('Arial', 24, 'bold'))
val_label.grid(row=1, column=1)

km_label = Label(text='Km', font=('Arial', 24, 'bold'))
km_label.grid(row=1, column=2)
 
button = Button(text='Calculate', command=convert)
button.grid(row=2, column=1)

    
window.mainloop()
    
    