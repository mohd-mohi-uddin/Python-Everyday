from tkinter import * 
from tkinter import ttk
from pathlib import Path
from password_generator1 import generate_password
from tkinter import messagebox
BASE_DIR = Path(__file__).parent

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def insert_password_generator():
    password = generate_password()
    password_input.delete(0,END)
    password_input.insert(0,password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website_name =website_input.get()
    email = email_input.get()
    my_password = password_input.get()

    if len(website_name) == 0 or len(email) == 0 or len(my_password) == 0:
        messagebox.showinfo(title="Oops!", message="You left some feilds empty, please type correctly.")
    else:
        is_ok = messagebox.askokcancel(title="Confirm Details",message= f'These are the detalis entered: \nWebsite: {website_name} \nEmail/Username: {email} \nPassword: {my_password} \n\n Press "ok" to save.')

        if is_ok:
            with open(BASE_DIR /"data.txt", mode= "a") as data:
                data.write(f"website name: {website_name}\nusername/email: {email}\npassword: {my_password}\n\n")

            for i in (website_input,email_input,password_input):
                i.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


"""canvas section"""
photoimage = PhotoImage(file= BASE_DIR /"logo.png")
canvas = Canvas(width=189,height=200)
canvas.create_image(100,102, image= photoimage)
canvas.grid(column=1, row= 0)


"""label section"""
website_label = ttk.Label(text= "Website:")
website_label.grid(column=0,row=1)
email_label = ttk.Label(text= "Email/Username:")
email_label.grid(column=0,row=2)
password_label = ttk.Label(text= "Password:")
password_label.grid(column=0,row=3)


"""entry section"""
website_input = ttk.Entry(width=50)
website_input.grid(column=1,row=1,columnspan=2)
website_input.focus()

email_input = ttk.Entry(width=50)
email_input.grid(column=1,row=2,columnspan=2)

password_input = ttk.Entry(width=31)
password_input.grid(column=1,row=3)


"""button section"""
password_button = ttk.Button(text="Generate Password", command=insert_password_generator)
password_button.grid(column=2,row=3)

add_button = ttk.Button(text="Add",width=49,command=save_password)
add_button.grid(column=1,row=4,columnspan=2)

window.mainloop()