import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("DATA")

# List to store user data
user_data = []

# Frame for the menu (Add Data, Show Data buttons)
menu_frame = tk.Frame(root)
menu_frame.pack(padx=20, pady=20)

# "Add Data" button
add_data_button = tk.Button(menu_frame, text="Add Data", width=20)
add_data_button.pack(pady=10)

# "Show Data" button
show_data_button = tk.Button(menu_frame, text="Show Data", width=20)
show_data_button.pack(pady=10)

# Frame for adding data (initially hidden)
add_data_frame = tk.Frame(root)

# Add a heading for Add Data form
heading = tk.Label(add_data_frame, text="User Information", font=("Arial", 16, "bold"))
heading.grid(row=0, column=0, columnspan=2, pady=10)

fields = ["Name", "Age", "Date of Joining", "Courses"]
entries = []

# Create labels and entry fields for the form inside the add_data_frame
for i, field in enumerate(fields[:-1]):  # Omit the last field ("Courses")
    label = tk.Label(add_data_frame, text=field)
    label.grid(row=i+1, column=0, padx=5, pady=5)
    
    entry = tk.Entry(add_data_frame, width=30)
    entry.grid(row=i+1, column=1, padx=5, pady=5)
    entries.append(entry)

# Create the "Courses" label
label = tk.Label(add_data_frame, text="Courses")
label.grid(row=len(fields), column=0, padx=5, pady=5)

# Create a Combobox for "Courses"
courses = ["BCA", "BSC IT", "BBA", "Btech", "Bsc"]
combobox = ttk.Combobox(add_data_frame, values=courses, width=28)
combobox.grid(row=len(fields), column=1, padx=5, pady=5)
combobox.set("Select a course")  # Set a default value
entries.append(combobox)

# Submit button
submit_button = tk.Button(add_data_frame, text="Submit", width=20)
submit_button.grid(row=len(fields)+1, column=0, columnspan=2, pady=10)

# Frame to show the data after submission
data_saved_frame = tk.Frame(root)

# Label to show data after submission
data_saved_label = tk.Label(data_saved_frame, text="Data Saved!", font=("Arial", 16, "bold"))
data_saved_label.grid(row=0, column=0, columnspan=2, pady=10)

# Text box to display submitted data in data_saved_frame
data_saved_display = tk.Text(data_saved_frame, height=10, width=50)
data_saved_display.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Button to go back to the main menu
go_back_button = tk.Button(data_saved_frame, text="Go Back", width=20)
go_back_button.grid(row=2, column=0, columnspan=2, pady=10)

# Frame to show all data when clicking "Show Data"
show_data_frame = tk.Frame(root)

# Add a heading for showing data
heading_show = tk.Label(show_data_frame, text="Submitted Data", font=("Arial", 16, "bold"))
heading_show.grid(row=0, column=0, columnspan=5, pady=10)

# Column headers for showing data in rows and columns
headers = ["Name", "Age", "Date of Joining", "Courses"]
for i, header in enumerate(headers):
    label = tk.Label(show_data_frame, text=header, font=("Arial", 12, "bold"), borderwidth=2, relief="ridge", width=15)
    label.grid(row=1, column=i, padx=5, pady=5)

# "Add More Data" button in show_data_frame
add_more_data_button = tk.Button(show_data_frame, text="Add More Data", width=20)
add_more_data_button.grid(row=2, column=0, columnspan=5, pady=10)

# Functions for frame switching

# Switch to the add data frame
def on_add_data_click(event):
    menu_frame.pack_forget()
    add_data_frame.pack(padx=20, pady=20)

# Switch to the show data frame
def on_show_data_click(event):
    menu_frame.pack_forget()
    show_data_frame.pack(padx=20, pady=20)
    
    # Clear previous data if any (only keep the headers)
    for widget in show_data_frame.grid_slaves():
        if int(widget.grid_info()["row"]) > 1 and int(widget.grid_info()["row"]) != 2:
            widget.destroy()

    # Display user data in tabular form
    for row_index, data in enumerate(user_data, start=2):
        tk.Label(show_data_frame, text=data["Name"], borderwidth=2, relief="ridge", width=15).grid(row=row_index, column=0, padx=5, pady=5)
        tk.Label(show_data_frame, text=data["Age"], borderwidth=2, relief="ridge", width=15).grid(row=row_index, column=1, padx=5, pady=5)
        tk.Label(show_data_frame, text=data["Date of Joining"], borderwidth=2, relief="ridge", width=15).grid(row=row_index, column=2, padx=5, pady=5)
        tk.Label(show_data_frame, text=data["Courses"], borderwidth=2, relief="ridge", width=15).grid(row=row_index, column=3, padx=5, pady=5)

# Switch to the data saved frame
def show_data_saved_frame():
    add_data_frame.pack_forget()
    data_saved_frame.pack(padx=20, pady=20)

# Go back to the main menu
def go_back_to_menu(event):
    data_saved_frame.pack_forget()
    show_data_frame.pack_forget()
    menu_frame.pack(padx=20, pady=20)

# Event when "Submit" button is clicked, to store the entered data and show the data_saved_frame
def on_submit_click(event):
    name = entries[0].get()
    age = entries[1].get()
    date_of_joining = entries[2].get()
    course = combobox.get()

    # Append the entered data to the user_data list
    user_data.append({
        "Name": name,
        "Age": age,
        "Date of Joining": date_of_joining,
        "Courses": course
    })
    
    # Clear the form fields after submission
    for entry in entries[:-1]:
        entry.delete(0, tk.END)
    combobox.set("Select a course")

    # Show the submitted data in data_saved_frame
    data_saved_display.delete(1.0, tk.END)
    data_saved_display.insert(tk.END, f"Name: {name}\n")
    data_saved_display.insert(tk.END, f"Age: {age}\n")
    data_saved_display.insert(tk.END, f"Date of Joining: {date_of_joining}\n")
    data_saved_display.insert(tk.END, f"Courses: {course}\n")
    
    # Switch to the data saved frame
    show_data_saved_frame()

# Function to go back to the Add Data form from the "Add More Data" button
def add_more_data(event):
    show_data_frame.pack_forget()
    add_data_frame.pack(padx=20, pady=20)



# Bindings and event handlers
add_data_button.bind("<Button-1>", on_add_data_click)
submit_button.bind("<Button-1>", on_submit_click)
show_data_button.bind("<Button-1>", on_show_data_click)
go_back_button.bind("<Button-1>", go_back_to_menu)
add_more_data_button.bind("<Button-1>", add_more_data)

root.mainloop()
