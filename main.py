from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def p_generator():
  
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
  
  nr_letters = random.randint(8, 10)
  nr_symbols = random.randint(2, 4)
  nr_numbers = random.randint(2, 4)
  
  password_letter=[random.choice(letters) for _ in range(nr_letters)]
  password_symbol=[random.choice(symbols) for _ in range(nr_symbols)]
  password_number=[random.choice(numbers) for _ in range(nr_numbers)]

  password_list = password_letter + password_symbol + password_number
  random.shuffle(password_list)
  
  password = "".join(password_list)
  
  
  password_t.insert(0,f"{password}")
  pyperclip.copy(f"{password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #

def data_file():
  inside_web = web_t.get()
  inside_email = email_t.get()
  inside_password = password_t.get()
  #print(f"{inside_web},{inside_email},{inside_password}")

  if inside_web=="" or inside_email == "" or inside_password == "":
    messagebox.showinfo(title = "Oops", message = "Please don't leave any fields empty!")

  else:
    is_ok = messagebox.askokcancel(title=inside_web, message= f"These are the details entered: \nEmail:{inside_email} \nPassword: {inside_password} \nIs it ok to save?")
  
    if is_ok:
      f = open("data.txt","a")
      f.write(f"{inside_web} | {inside_email} | {inside_password}\n")
      f.close()
      web_t.delete(0,'end')
      password_t.delete(0,"end")
      web_t.focus()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
#window.minsize(width=440,height=440)
window.config(padx=50, pady=50)

img_l= PhotoImage(file="logo.png")
canvas= Canvas(width=200, height=200)
canvas.create_image(100, 100, image=img_l)
canvas.grid(column=1, row=0)

# Add "Website" lable and textbox
web = Label(text="Website:", font=("Arial", 10, "bold"))
web.grid(column=0, row=1)

web_t = Entry(width=35)
web_t.grid(row=1, column=1, columnspan = 2)
web_t.focus()

# Add Email/Username and textbox

email=Label(text="Email/Username:", font=("Arial", 10, "bold") )
email.grid(column=0,row=2)

email_t = Entry(width=35)
email_t.grid(row=2, column=1, columnspan = 2)
email_t.insert(0,"v@gmail.com")


# Add Password and textbox and button for password generation

password = Label(text="Password:", font=("Arial", 10, "bold"))
password.grid(column=0, row=3)

password_t = Entry(width = 18)
password_t.grid(column=1, row=3)

password_g= Button(text="Generate Password", command=p_generator)
password_g.grid(column=2, row=3)


# Add Button

add = Button(text="Add", width=36, command = data_file)
add.grid(row=4, column=1, columnspan=2)


window.mainloop()