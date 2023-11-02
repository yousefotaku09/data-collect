# Import tkinter and filedialog modules
from tkinter import *
from tkinter import filedialog

# Create a tkinter window
space = Tk()
space.geometry("1025x1025")
space.title("ادخال البيانات")

# Define a function to save the data to a file
def save_file():
    # Get the data from the entry widgets
    name = name_entry.get()
    birth = birth_entry.get()
    adress = adress_entry.get()
    phone_number = phone_number_entry.get()
    # Create a tuple of the data
    data_entry = (name, birth, adress, phone_number)
    # Ask the user to choose a directory and a file name
    file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    # If the user chooses a file, write the data to it
    if file is not None:
        # Convert the tuple to a string
        text_to_save = str(data_entry)
        # Write the string to the file
        file.write(text_to_save)
        # Close the file
        file.close()

# Define a function to browse for a file
def browse_file():
    # Ask the user to choose a file
    file = filedialog.askopenfile(mode='r', defaultextension=".txt")
    # If the user chooses a file, read the data from it
    if file is not None:
        # Read the string from the file
        text_to_read = file.read()
        # Convert the string to a tuple
        data_entry = eval(text_to_read)
        # Close the file
        file.close()
        # Set the data to the entry widgets
        name_entry.delete(0, END)
        name_entry.insert(0, data_entry[0])
        birth_entry.delete(0, END)
        birth_entry.insert(0, data_entry[1])
        adress_entry.delete(0, END)
        adress_entry.insert(0, data_entry[2])
        phone_number_entry.delete(0, END)
        phone_number_entry.insert(0, data_entry[3])

# Create entry widgets for name, birth, adress, and phone number
name_entry = Entry(width=50)
birth_entry = Entry(width=50)
adress_entry = Entry(width=50)
phone_number_entry = Entry(width=50)

# Create label widgets for name, birth, adress, and phone number
label_name = Label(text="enter your name:")
label_birth = Label(text="enter your birth:")
label_adress = Label(text="enter your adress:")
label_phone_number = Label(text="enter your phone number:")

# Create button widgets for save and browse
button_save = Button(text="save", width=10, command=save_file)
button_browse = Button(text="browse", width=5, command=browse_file)

# Arrange the widgets using the place method with x and y coordinates
label_name.place(x=50, y=50)
name_entry.place(x=150, y=50)
label_birth.place(x=50, y=100)
birth_entry.place(x=150, y=100)
label_adress.place(x=50, y=150)
adress_entry.place(x=150, y=150)
label_phone_number.place(x=50,y=200)
phone_number_entry.place(x=150,y=200)
button_save.place(x=275,y=250,width=100,height=30)
button_browse.place(x=400,y=250,width=50,height=30)

# Start the main loop of the window
space.mainloop()
