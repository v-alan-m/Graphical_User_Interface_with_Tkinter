from tkinter import *

# Create the window object
window = Tk()

# This function is assigned to the command arguement 
# The function will run on pressing pressing the button
def km_to_miles():
    miles_conv = float(d1_value.get()) * 1.6
    t1.delete("1.0", END) 
    t1.insert(END, miles_conv)

# Generate a button widget
# The 'button' will be assigned to 'window'
# Label the button using the 'text' arguement
# This function is assigned to the command arguement to do so
b1 = Button(window, text="Execute", command=km_to_miles)

''' 
Position 'button' within 'window' uisng pack() or grid()
grid() allows for greater control of positioning
'''
b1.grid(row=0,column=0)

# Create a variable for the data entry
d1_value = StringVar()

# The variable will be feed into the function
d1 = Entry(window, textvariable=d1_value)
d1.grid(row=0,column=1)

# Text widget
# Specify the size of the text box
t1 = Text(window,height=1,width=20)
t1.grid(row=0,column=2)

'''
Keep the window open until the window is closed.
Otherwise, the window will open and the close immedately
'''
window.mainloop()