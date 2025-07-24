from tkinter import *
from tkinter import messagebox
import random
import pyperclip


def generate_password():
    pass_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    password_list = [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(numbers) for num in range(nr_symbols)]
    password_list += [random.choice(symbols) for sym in range(nr_numbers)]
    random.shuffle(password_list)
    password = "".join(password_list)
    pass_input.insert(0, password)
    pyperclip.copy(password)
    messagebox.showinfo(message="Copied to clipboard")


window = Tk()
window.title("SecureNest")
window.config(padx=50, pady=50)


def add_entry():
    website = website_input.get()
    email = email_input.get()
    _pass = pass_input.get()

    if len(website) == 0 or len(email) == 0 or len(_pass) == 0:
        messagebox.showerror(title="Empty Fields", message="Do not leave any field Empty")
    else:
        info_confirmed = messagebox.askokcancel(title=website, message=f"Confirm Details\nEmail: "f"{email}\nPassword"
                                                                       f": {_pass}")
        if info_confirmed:
            with open("data.txt", "a") as file:
                file.write(website + " | " + email + " | " + _pass + '\n')
            website_input.delete(0, END)
            email_input.delete(0, END)
            pass_input.delete(0, END)
            website_input.focus()


canvas = Canvas(height=240, width=842)
logo = PhotoImage(file="logo1.png")
canvas.create_image(421, 120, image=logo)
canvas.grid(column=1, columnspan=3, row=1, pady=(50, 80))

website_label = Label(text="Website:", font=("Ariel", 15))
website_label.grid(column=1, row=2, padx=(150, 0))

website_input = Entry(width=70)
website_input.grid(column=2, row=2, columnspan=2, padx=(0, 120))
website_input.focus()

email_label = Label(text="Email/username:", font=("Ariel", 15))
email_label.grid(column=1, row=3, padx=(120, 0))

email_input = Entry(width=70)
email_input.grid(column=2, row=3, columnspan=2, padx=(0, 120))

password_label = Label(text="Password:", font=("Ariel", 15))
password_label.grid(column=1, row=4, padx=(140, 0))

pass_input = Entry(width=40)
pass_input.grid(column=2, row=4)

generate_pass_button = Button(text="Generate Password", command=generate_password)
generate_pass_button.grid(column=3, row=4, padx=(0, 170))

add_entry_button = Button(text="Add Entry", width=60, command=add_entry)
add_entry_button.grid(column=2, row=5, columnspan=2, pady=20, padx=(0, 120))

window.mainloop()
