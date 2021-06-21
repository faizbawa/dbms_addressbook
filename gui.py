from tkinter import *
from tkinter import Entry


import sqlite3

root = Tk()
root.geometry("350x500")
root.title("Address Book App")

# Database
# Create a database or connect to one
conn = sqlite3.connect('address_book.db')

# Create cursor
c = conn.cursor()

# Create Table
'''
c.execute("""CREATE TABLE addresses (
        first_name text,
        last_name text,
        address text,
        city text,
        state text,
        zipcode integer)
""")
'''

# create a edit func to update record
def update():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    c = conn.cursor()

    record_id = delete_box.get()

    c.execute('''UPDATE addresses SET
        first_name = :first,
        last_name = :last,
        address = :address,
        city = :city,
        state = :state,
        zipcode = :zipcode
        
        WHERE oid = :oid''',
              {
                 'first': f_name.get(),
                  'last': l_name.get(),
                  'address': address.get(),
                  'city': city.get(),
                  'state': state.get(),
                  'zipcode': zipcode.get(),

                  'oid': record_id
              }
        )


    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close()

    editor.destroy()




# Create Update record
def edit():
    global editor
    editor = Tk()
    editor.geometry("350x200")
    editor.title("Update record")

    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    c = conn.cursor()

    record_id = delete_box.get()
    # QUery the Database
    c.execute("SELECT * FROM addresses WHERE oid = " + record_id)
    records = c.fetchall()

    # Create Global Variables for text box names to use in update func
    global f_name
    global l_name
    global address
    global city
    global state
    global zipcode



    # Create text Boxes
    f_name = Entry(editor, width=30)
    f_name.grid(row=0, column=1, padx=20, pady=(10, 0))
    l_name = Entry(editor, width=30)
    l_name.grid(row=1, column=1, padx=20)
    address = Entry(editor, width=30)
    address.grid(row=2, column=1, padx=20)
    city = Entry(editor, width=30)
    city.grid(row=3, column=1, padx=20)
    state = Entry(editor, width=30)
    state.grid(row=4, column=1, padx=20)
    zipcode = Entry(editor, width=30)
    zipcode.grid(row=5, column=1, padx=20)

    # Create textbox labels
    f_name1 = Label(editor, text="First Name")
    f_name1.grid(row=0, column=0, pady=(10, 0))
    l_name1 = Label(editor, text="Last Name")
    l_name1.grid(row=1, column=0)
    address1 = Label(editor, text="Address")
    address1.grid(row=2, column=0)
    city1 = Label(editor, text="City")
    city1.grid(row=3, column=0)
    state1 = Label(editor, text="State")
    state1.grid(row=4, column=0)
    zipcode1 = Label(editor, text="Zipcode")
    zipcode1.grid(row=5, column=0)

    # Loop thru results
    for record in records:
        f_name.insert(0, record[0])
        l_name.insert(0, record[1])
        address.insert(0, record[2])
        city.insert(0, record[3])
        state.insert(0, record[4])
        zipcode.insert(0, record[5])

    # create a save button
    edit_btn = Button(editor, text="Save Record", command=update)
    edit_btn.grid(row=11, column=0, columnspan=2, padx=10, pady=10, ipadx=125)

# Create function to delete records
def delete():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    c = conn.cursor()

    # Delete a record
    c.execute("DELETE FROM addresses WHERE oid = " + delete_box.get())

    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close()

    delete_box.delete(0, END)




# Create Submit function
def submit():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    c = conn.cursor()

    # Insert into table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
        {
            'f_name': f_name.get(),
            'l_name': l_name.get(),
            'address': address.get(),
            'city': city.get(),
            'state': state.get(),
            'zipcode': zipcode.get()
        })


    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close()

    # Clear text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)


# create query Function
def query():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    c = conn.cursor()

    # QUery the Database
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    #print(records)

    # Loop thruogh results
    print_records = ''
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + "\t" + str(record[6]) + "\n"

    query_label = Label(root,text=print_records)
    query_label.grid(row=12, column=0, columnspan=2)



    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close()











# Create text Boxes
f_name = Entry(root,width=30)
f_name.grid(row=0,column=1,padx=20, pady=(10,0))
l_name = Entry(root,width=30)
l_name.grid(row=1,column=1,padx=20)
address = Entry(root,width=30)
address.grid(row=2,column=1,padx=20)
city = Entry(root,width=30)
city.grid(row=3,column=1,padx=20)
state = Entry(root,width=30)
state.grid(row=4,column=1,padx=20)
zipcode = Entry(root,width=30)
zipcode.grid(row=5,column=1,padx=20)
delete_box = Entry(root, width =20)
delete_box.grid(row=9, column=1, padx=20)

# Create textbox labels
f_name1 = Label(root, text="First Name")
f_name1.grid(row=0,column=0, pady=(10,0))
l_name1 = Label(root, text="Last Name")
l_name1.grid(row=1,column=0)
address1 = Label(root, text="Address")
address1.grid(row=2,column=0)
city1 = Label(root, text="City")
city1.grid(row=3,column=0)
state1 = Label(root, text="State")
state1.grid(row=4,column=0)
zipcode1 = Label(root, text="Zipcode")
zipcode1.grid(row=5,column=0)
delete_box_label = Label(root,text="Select ID")
delete_box_label.grid(row=9,column=0,pady = 5)

# Create Submit Button
submit_btn = Button(root, text="Add Record to Database", command = submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# create a query button
query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, padx=10, pady=10, ipadx=125)

# create a delete button
delete_btn = Button(root, text="Delete Record", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, padx=10, pady=10, ipadx=125)

# create an Update button
edit_btn = Button(root, text="Update Record", command=edit)
edit_btn.grid(row=11, column=0, columnspan=2, padx=10, pady=10, ipadx=125)
# Commit Changes
conn.commit()

# Close Connection
conn.close()


root.mainloop()
