# ---------------------------- PASSWORD GENERATOR ------------------------------- #

import random
# 외부 라이브러리라 pip install pyperclip 해야 함. Generate Password 버튼 누르면 자동으로 copy해서 paste할 수 있게 만드는 라이브러리임
import pyperclip

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    #list comprehension

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)

    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)


    pwd_letters =  [ random.choice(letters) for char in range(nr_letters)]
    pwd_symbols = [random.choice(symbols) for char in range(nr_symbols)]
    pwd_numbers = [random.choice(numbers) for char in range(nr_numbers)]
    password_list = pwd_letters + pwd_symbols + pwd_numbers

    random.shuffle(password_list)

    password = "".join(password_list)


    pwd_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *
from tkinter import messagebox
def save():
    web_name = web_entry.get()
    email_addr = email_username_entry.get()
    pwd = pwd_entry.get()
    
    # validation test, 웹사이트나 비밀번호란이 비어있을 때
    if len(web_name) == 0 or len(pwd) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")
        
    else:
        # 입력 정보 확인
        is_ok = messagebox.askokcancel(title=web_name, message=f"These are the details entered: \nEmail: {email_addr}\nPassword:{pwd} \nIs it ok to save?")
        
        if is_ok:
            with open('data.txt', mode='a', encoding='utf-8') as f:
                f.write(f"{web_name} | {email_addr} | {pwd}\n")
        
            web_entry.delete(0, END)
            pwd_entry.delete(0,END)
        
    
   

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg='white')

# image
canvas = Canvas(width=200, height=200, bg='white', highlightthickness=0)
logo_img = PhotoImage(width=200, height=200, file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)


# 'website' label

web_label = Label(text="Website:", bg='white', highlightthickness=0)
web_label.grid(row=1, column=0)

# 'website' entry

web_entry = Entry(width=35)
# 시작하자마자 입력 필드에 포커싱
web_entry.focus()
web_entry.grid(row=1, column=1, columnspan=2)

# 'Emali/Username' label

email_username_label = Label(text="Email/Username:", bg='white', highlightthickness=0)
email_username_label.grid(row=2, column=0)

# 'Email/Username' entry

email_username_entry = Entry(width=35)
email_username_entry.insert(0, string="dmsqo122@naver.com")
email_username_entry.grid(row=2, column=1, columnspan=2)

# 'Password' Label

pwd_label = Label(text="Password:", bg='white', highlightthickness=0)
pwd_label.grid(row=3, column=0)

# 'Password' entry

pwd_entry = Entry(width=21)
pwd_entry.grid(row=3, column=1)

# 'generate_pwd' button 

generate_pwd_btn = Button(width= 15, text="Generate Password", command=generate_password)
generate_pwd_btn.grid(row=3, column=2)

# 'Add' button 

add_btn = Button(width=36, text="Add", command=save)
add_btn.grid(row=4, column=1, columnspan=2)









window.mainloop()