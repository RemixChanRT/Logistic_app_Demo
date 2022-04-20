from user_creation import *
from document_type import *
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
generator_frame.grid(row=3, column=0)

street_receive = Entry(document_frame)
zip_receive = Entry(document_frame)
city_receive = Entry(document_frame)
receive_label = Label(document_frame, text="From:")
receive_label.grid(row=0, column=0)
street1 = Label(document_frame, text="Street")
street1.grid(row=1, column=0)
street_receive.grid(row=2, column=0)
zip1 = Label(document_frame, text="Zip")
zip1.grid(row=3, column=0)
zip_receive.grid(row=4, column=0)
city1 = Label(document_frame, text="City")
city1.grid(row=5, column=0)
city_receive.grid(row=6, column=0)

receiver_name = Entry(document_frame)
street_deliver = Entry(document_frame)
zip_deliver = Entry(document_frame)
city_deliver = Entry(document_frame)
deliver_label = Label(document_frame, text="To:")
deliver_label.grid(row=7, column=0)
name1 = Label(document_frame, text="Name")
name1.grid(row=8, column=0)
receiver_name.grid(row=9, column=0)
street2 = Label(document_frame, text="Street")
street2.grid(row=10, column=0)
street_deliver.grid(row=11, column=0)
zip2 = Label(document_frame, text="Zip")
zip2.grid(row=12, column=0)
zip_deliver.grid(row=13, column=0)
city2 = Label(document_frame, text="City")
city2.grid(row=14, column=0)
city_deliver.grid(row=15, column=0)

primary_contact = Entry(document_frame)
secondary_contact = Entry(document_frame)
primary1 = Label(document_frame, text="Primary Contact")
primary1.grid(row=16, column=0)
primary_contact.grid(row=17, column=0)
secondary1 = Label(document_frame, text="Second Contact")
secondary1.grid(row=18, column=0)
secondary_contact.grid(row=19, column=0)

list_items = Entry(document_frame)
items1 = Label(document_frame, text="List Items")
items1.grid(row=20, column=0)
list_items.grid(row=21, column=0)


def generated_doc():
    doc_created = Toplevel()
    doc_created.title("Generated Document")
    doc_created.geometry("645x500")
    # This is the text widget that will show the generated documents of your choice
    global document
    document_label = Label(doc_created, text="Generated Document")
    document_label.grid(row=0, column=0)

    document = Text(doc_created)

    document.config(state="normal")
    document.insert("1.0", shipping_doc)
    document.config(state="disabled")

    document.grid(row=1, column=0)


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


def shipping_manifest():
    global shipping_doc
    shipping_doc = str(
        "\n" + "Pol-Logistics shipping manifest\n" + "\n" + "[Name of the shipment determined by client]" + "\n" + "\n" +
        "Directions: Place the manifest in a zip-loc bag and place it on top\nof the shipping container\n" +
        "---------------------------------------------------------------------\n\n" +
        "General Information:\n" +
        "Shipped by: " + str(bus_name.get()) + "\n"
                                               "Sent from: \n" +
        str(street_receive.get()) + "\n" +
        str(zip_receive.get()) + " " + str(city_receive.get()) + "\n\n" +
        "Contact information: \n" +
        "Primary contact: " + str(primary_contact.get()) + "\n" +
        "Secondary contact: " + str(secondary_contact.get()) + "\n" +
        "\nThe shipment contains the following:\n" +
        str(list_items.get()) + "\n\n" +
        "Delivery Address:\n" +
        str(receiver_name.get()) + "\n" +
        str(street_deliver.get()) + "\n" +
        str(zip_deliver.get()) + " " + str(city_deliver.get()) + "\n\n" +
        "Driver Signature: \n\n __________________________"
    )
    generated_doc()


# Create Document Button
shipping_button = Button(generator_frame, text="Generate Shp. Manifest", command=shipping_manifest, width=20, height=2)
shipping_button.grid(row=0, column=0)
cargo_button = Button(generator_frame, text="Generate Trn. Manifest", command=shipping_manifest, width=20, height=2)
cargo_button.grid(row=0, column=1)

# Create new user button!
new_user = Button(data_frame, text="Create new User", command=uc, width=20, height=2)
new_user.grid(row=0, column=0, padx=5, pady=5)
# Load existing user button
load_user = Button(data_frame, text="Load existing User", command=user_load, width=20, height=2)
load_user.grid(row=0, column=1, padx=5, pady=5)
# Manifest Generator
manifest = Button

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
