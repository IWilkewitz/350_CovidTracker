from tkinter import *
import sqlite3

root = Tk()
root.title("Test window")
root.geometry("400x400")

# Databases

# Create a databse or connect to one
conn = sqlite3.connect('user_info_db.db')

# Create cursor
c = conn.cursor()

# Create table
c.execute("""CREATE TABLE user_info (
#         first_name text,
#         last_name text,
#         address text,
#         city text,
#         state text,
#         zipcode integer
#         )""")

# Create submission
def submit():
    # Create a databse or connect to one
    conn = sqlite3.connect('user_info_db.db')

    # Create cursor
    c = conn.cursor()

    # Insert into table
    c.execute("INSERT INTO user_info VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
            {
                'f_name': f_name.get(),
                'l_name': l_name.get(),
                'address': address.get(),
                'city': city.get(),
                'state': state.get(),
                'zipcode': zipcode.get()
            }

            )

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()

    # Clear the text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

# Create query function
def query():
    # Create a databse or connect to one
    conn = sqlite3.connect('user_info_db.db')

    # Create cursor
    c = conn.cursor()

    # Query the DB
    c.execute("SELECT *, oid FROM user_info") # OID is primary key
    records = c.fetchall() # get all records (must be changed for current user)
    # print(records) # prints records to the terminal after closing

    # Parse results
    print_records = ''
    for record in records:
        print_records += str(record[0]) + "\n" # print first name(s)

    query_label = Label(root, text = print_records)
    query_label.grid(row = 8, column = 0, columnspan = 2)

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()

# Create text boxes
f_name = Entry(root, width = 30)
f_name.grid(row = 0, column = 1, padx = 20)

l_name = Entry(root, width = 30)
l_name.grid(row = 1, column = 1)

address = Entry(root, width = 30)
address.grid(row = 2, column = 1)

city = Entry(root, width = 30)
city.grid(row = 3, column = 1)

state = Entry(root, width = 30)
state.grid(row = 4, column = 1)

zipcode = Entry(root, width = 30)
zipcode.grid(row = 5, column = 1)

# Create text box labels
f_name_label = Label(root, text = "First name")
f_name_label.grid(row = 0, column = 0)

l_name_label = Label(root, text = "Last name")
l_name_label.grid(row = 1, column = 0)

address_label = Label(root, text = "Address")
address_label.grid(row = 2, column = 0)

city_label = Label(root, text = "City")
city_label.grid(row = 3, column = 0)

state_label = Label(root, text = "State")
state_label.grid(row = 4, column = 0)

zipcode_label = Label(root, text = "Zipcode")
zipcode_label.grid(row = 5, column = 0)

# Create submit button
submit_btn = Button(root, text = "Save to DB", command = submit)
submit_btn.grid(row = 6, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 60)

# Create query button
query_btn = Button(root, text = "Show records", command = query)
query_btn.grid(row = 7, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 140)



# Commit changes
conn.commit()

# Close connection
conn.close()

root.mainloop()
