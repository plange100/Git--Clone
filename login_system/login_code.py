from tkinter import *
import os

def main_menu():
  global main_window
  main_window = Tk()
  main_window.geometry("300x300")
  main_window.title("Login System")
  label1 = Label(main_window, text="Choose an option", bg="gray", fg="blue")
  label1.pack(fill=X,pady=20)
  login_button = Button(main_window, text="Log in", width="30", height="2", command=login)
  login_button.pack(pady=20)
  register_button = Button(main_window, text="Register", width="30", height="2", command=register)
  register_button.pack(pady=20)
  main_window.mainloop()


def register():

  global username
  global password
  global fullname
  global username_entry
  global password_entry
  global fullname_entry
  global register_window

  register_window = Toplevel(main_window)
  register_window.title("Register New User")
  register_window.geometry("300x300")

  username = StringVar()
  password = StringVar()
  fullname = StringVar()

  label2 = Label(register_window, text="Please fill in the info below", bg="gray", fg="blue")
  label2.pack(fill=X,pady=20)

  register_window_panel = Frame(register_window)
  register_window_panel.pack(pady=20)

  username_label = Label(register_window_panel, text="Username: ")
  username_label.grid(row=0, column=0)
  username_entry = Entry(register_window_panel, textvariable=username)
  username_entry.grid(row=0, column=1)

#emtpy row to create space
  Label(register_window_panel, text="").grid(row=1)

  password_label = Label(register_window_panel, text="Password: ")
  password_label.grid(row=2, column=0)
  password_entry = Entry(register_window_panel, textvariable=password)
  password_entry.grid(row=2, column=1)

#emtpy row to create space
  Label(register_window_panel, text="").grid(row=3)

  fullname_label = Label(register_window_panel, text="Full Name: ")
  fullname_label.grid(row=4, column=0)
  fullname_entry = Entry(register_window_panel, textvariable=fullname)
  fullname_entry.grid(row=4, column=1)

  register_button1 = Button(register_window, text="Register", width="30", height="2",command=register_user)
  register_button1.pack()


def register_user():
  registered = False
  username_text = username.get()
  password_text = password.get()
  fullname_text = fullname.get()

  file = open("login_system/credentials.txt", "a")
  for line in open("login_system/credentials.txt", "r").readlines():
    login_info = line.split()
    if username_text == login_info[1]:
      registered = True
  if registered:
    file.close()
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    fullname_entry.delete(0, END)
    user_exists_window = Toplevel(main_window)
    user_exists_window.geometry("200x200")
    user_exists_window.title("User exists")
    Label(user_exists_window, text="User already exists", bg="gray", fg="blue").pack(fill=X,pady=20)
    exists_button = Button(user_exists_window, text="User already exists, try again", width="20", command= lambda :user_exists_window.destroy())
    exists_button.pack(pady=20)
  else:
    file.write("Username: " + username_text + " Password: " + password_text + " Name: " + fullname_text+"\n")
    file.close()
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    fullname_entry.delete(0, END)
    success_register_window = Toplevel(register_window)
    success_register_window.geometry("200x200")
    success_register_window.title("Success!")
    Label(success_register_window, text="Successful Registration", bg="gray", fg="blue").pack(fill=X,pady=20)
    ok_button = Button(success_register_window, text="OK", width="20", command= lambda :success_register_window.destroy())
    ok_button.pack(pady=20)

def login():
  #create global variables for username and password
  global username_prompt
  global password_prompt
  global username_verify
  global password_verify
  global login_window

  #create login window using Toplevel, geometry, title
  login_window = Toplevel(main_window)
  login_window.geometry("300x300")
  login_window.title("login")

  #create label for userame and password and pack it
  label2 = Label(login_window,text="Please enter username and password", bg='gray', fg="blue")
  label2.pack(fill=X, pady=20)

  #create frame to create entry prompts
  credentials_panel = Frame(login_window)
  credentials_panel.pack(pady=20)

  #create StringVar for username and password
  username_verify = StringVar()
  password_verify = StringVar()

  #create username label in credentials panel and entry prompt box
  username_label = Label(credentials_panel, text="Username: ")
  username_label.grid(row=0, column=0)
  username_prompt = Entry(credentials_panel, textvariable=username_verify)
  username_prompt.grid(row=0, column=1)

  #emtpy row to create space
  Label(credentials_panel, text="").grid(row=1)

  #create password label in credentials panel and entry prompt box
  password_label = Label(credentials_panel, text="Password: ")
  password_label.grid(row=2, column=0)
  password_prompt = Entry(credentials_panel, textvariable=password_verify)
  password_prompt.grid(row=2, column=1)

  #create login button
  login_button = Button(login_window, text="Login", command=login_verify)
  login_button.pack(pady=20)


def login_verify():

  registered = False
  #get username and password
  username_get = username_verify.get()
  password_get = password_verify.get()

  #read credentials.txt to verify user
  file = open("login_system/credentials.txt")
  for line in open("login_system/credentials.txt", "r").readlines():
    login_info = line.split()
    if username_get == login_info[1] and password_get == login_info[3]:
      registered = True
  if registered:
    file.close()
    #create successful login window using Toplevel, geometry, title
    is_verify_window = Toplevel(login_window)
    is_verify_window.geometry("200x200")
    is_verify_window.title("Login verified")
  else:
    #if entered data is not in credentials.txt
    not_verify_window = Toplevel(login_window)
    not_verify_window.geometry("200x200")
    not_verify_window.title("Login failed")
    #delete prompts
    username_prompt.delete(0, END)
    password_prompt.delete(0, END)
    Label(not_verify_window, text="Login Failed", bg="gray", fg="blue").pack(fill=X,pady=20)
    ok_button = Button(not_verify_window, text="OK", width="20", command= lambda :not_verify_window.destroy())
    ok_button.pack(pady=20)
  
  



main_menu()