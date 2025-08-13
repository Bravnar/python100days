from tkinter import *
from tkinter import messagebox
import pyperclip
from password_generator import generator

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password_entry.delete(0, END)
    password = generator()
    pyperclip.copy(password)
    password_entry.insert(END, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def check_password(password):
    length = len(password) > 7
    has_number = len([x for x in password if x.isdigit()]) > 0
    print(has_number)
    has_symbol = len([x for x in password if x in ['!', '#', '$', '%', '&', '(', ')', '*', '+']]) > 0
    print(has_symbol)

    if (length and has_number and has_symbol): return True
    else:
        message = f"Password must contain:\nAt least 8 characters\nA number\nA special symbol ('#!@*/+-=$')"
        messagebox.showerror(title="Invalid Password", message=message)
        return False


def check_email(email):
    
    has_at = '@' in email
    valid_extension = email.split('.')[-1] in ("com", "ch", "fr", "me", "it", "ru")

    if has_at and valid_extension: return True
    else: 
        messagebox.showerror(title=email, message="Invalid e-mail")
        return False
    

def save_to_file():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if not (website and email and password):
        messagebox.showinfo(title="Empty fields", message="Please fill in all the fields")
        return
    
    if not check_email(email) or not check_password(password):
        return
    
    is_ok = messagebox.askokcancel(
        title=website, message=f"""
Information provided:

Website:{website}
Email:{email}
Password:{password}

    Is it OK to save?"""
    )

    if not is_ok:
        return

    with open("data.txt", "a") as file:
        file.write(f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n")
        # warning_label.config(text="Password added successfully.", fg="green")
        website_entry.delete(0, END)
        password_entry.delete(0, END)
        website_entry.focus()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas =  Canvas(width=200, height=200)
my_pass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=my_pass_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky="nw")
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky="new")

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0, sticky="nw")
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky="new")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky="nw")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="new")

genpassword_btn = Button(text="Password", command=generate_password)
genpassword_btn.grid(row=3, column=2, sticky="new")

add_btn = Button(text="Add", width=36, command=save_to_file)
add_btn.grid(row=4, column=1, columnspan=2, sticky="new")

warning_label = Label(fg="red")
warning_label.grid(row=5, column=1)

website_entry.focus()
email_entry.insert(END, "brav@ik.me")


window.mainloop()