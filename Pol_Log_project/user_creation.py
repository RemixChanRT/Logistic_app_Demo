from tkinter import *
from tkinter import filedialog

user_id = 0


# Function that will pop up a window with user creation Options
def uc():
    user_creation = Toplevel()
    user_creation.title("New User")
    user_creation.geometry("700x350")

    global business_id, business_name, business_owner, est_value, business_category, business_id, user_notes
    # What is the companies name
    bus_label = Label(user_creation, text="Business Name: ")
    bus_label.grid(row=0, column=0, pady=5)

    business_name = Entry(user_creation, width=15)
    business_name.grid(row=0, column=1, padx=10, pady=5)

    # Who's the business owner
    bus_owner = Label(user_creation, text="Owner Name: ")
    bus_owner.grid(row=0, column=2, padx=5, pady=5)

    business_owner = Entry(user_creation, width=15)
    business_owner.grid(row=0, column=3, padx=10, pady=5)

    # Estimated Value of moved product
    bus_val = Label(user_creation, text="Est. product value: ")
    bus_val.grid(row=2, column=0, padx=10, pady=5)

    est_value = Entry(user_creation, width=15)
    est_value.grid(row=2, column=1, padx=10, pady=5)

    # The Category of the business
    bus_cat = Label(user_creation, text="Business Category: ")
    bus_cat.grid(row=2, column=2, padx=10, pady=5)

    business_category = Entry(user_creation, width=15)
    business_category.grid(row=2, column=3, padx=10, pady=5)

    bus_id = Label(user_creation, text="BUID: ")
    bus_id.grid(row=0, column=4, padx=10, pady=5)

    business_id = Entry(user_creation, width=15)
    business_id.grid(row=0, column=5, padx=10, pady=5)

    id_gen = Button(user_creation, text="GENERATE", width=15, command=id_generator)
    id_gen.grid(row=2, column=5, padx=10, pady=5)

    user_notes = Text(user_creation, width=55, height=15)
    user_notes.grid(row=3, column=0, columnspan=4)

    save_button1 = Button(user_creation, text="Save", height=15, width=15, command=user_save)
    save_button1.grid(row=3, column=5)


# User ID Generation
def id_generator():
    global user_id
    business_id.delete(0, END)
    user_id += 1
    business_id.insert(0, str(user_id))


# New User Saving function
def user_save():
    newu = [business_name.get(), business_owner.get(), est_value.get(), business_category.get(), business_id.get(),
            user_notes.get("1.0", END)]
    print(newu)
    path = filedialog.asksaveasfile(initialdir="/", title="Save file",
                                    filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
    for element in newu:
        path.write(element + "\n")
    pass