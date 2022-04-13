from user_creation import *
from tkinter import *

# The Root window in which everything is displayed
root = Tk()
root.title("Pol-Log v0.1")
root.geometry("1600x600")

name_frame = Frame(root)
name_frame.grid(row=0, column=0)

program_name = Label(name_frame, text="Welcome to Pol-Log, the best logistics system you'll never use!")
program_name.grid(row=0, column=0, pady=15, padx=15)

data_frame = Frame(root)
data_frame.grid(row=1, column=0)

document_frame = Frame(root)
document_frame.grid(row=0, column=1, rowspan=4)

generator_frame = Frame(root)
generator_frame.grid(row=3, column=0, columnspan=2)


def user_load():
    user = []
    path = filedialog.askopenfile(initialdir="/", title="Select file",
                                  filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
    if path is not None:
        content = path.readlines()
        for line in content:
            user.append(line.strip("\n"))
    print(user)

    bus_name.config(state="normal")
    own_name.config(state="normal")
    prod_val.config(state="normal")
    bus_category.config(state="normal")
    bu_id.config(state="normal")

    bus_name.delete(0, END)
    own_name.delete(0, END)
    prod_val.delete(0, END)
    bus_category.delete(0, END)
    bu_id.delete(0, END)

    bus_name.insert(0, string=user[0])
    own_name.insert(0, string=user[1])
    prod_val.insert(0, string=user[2])
    bus_category.insert(0, string=user[3])
    bu_id.insert(0, string=user[4])

    bus_name.config(state="readonly")
    own_name.config(state="readonly")
    prod_val.config(state="readonly")
    bus_category.config(state="readonly")
    bu_id.config(state="readonly")

    pass


# Create new user button!
new_user = Button(data_frame, text="Create new User", command=uc, width=20, height=2)
new_user.grid(row=0, column=0, padx=5, pady=5)
# Load existing user button
load_user = Button(data_frame, text="Load existing User", command=user_load, width=20, height=2)
load_user.grid(row=0, column=1, padx=5, pady=5)
# Manifest Generator
manifest = Button

# This is the text widget that will show the generated documents of your choice
document = Text(document_frame, width=80, height=20, state="disabled")
document.grid(row=1, column=0)

# Below will be loaded information from the user loading part.
# Entry widgets that show loaded data
bus_name = Entry(data_frame, width=15, state="readonly", readonlybackground="white")
own_name = Entry(data_frame, width=15, state="readonly", readonlybackground="white")
prod_val = Entry(data_frame, width=15, state="readonly", readonlybackground="white")
bus_category = Entry(data_frame, width=15, state="readonly", readonlybackground="white")
bu_id = Entry(data_frame, width=15, state="readonly", readonlybackground="white")

# Label Frames
name_label = Label(data_frame, text="Business Name:")
owner_label = Label(data_frame, text="Owner Name:")
product_label = Label(data_frame, text="Est. Product value:")
business_label = Label(data_frame, text="Category")
id_label = Label(data_frame, text="ID")
category1 = Label(data_frame, text="User Data: ")

# The Grid layout
category1.grid(row=1, column=0, columnspan=2, pady=5)
name_label.grid(row=2, column=0, pady=5)
owner_label.grid(row=3, column=0, pady=5)
product_label.grid(row=4, column=0, pady=5)
business_label.grid(row=5, column=0, pady=5)
id_label.grid(row=6, column=0, pady=5)

bus_name.grid(row=2, column=1, pady=5)
own_name.grid(row=3, column=1, pady=5)
prod_val.grid(row=4, column=1, pady=5)
bus_category.grid(row=5, column=1, pady=5)
bu_id.grid(row=6, column=1, pady=5)

root.mainloop()