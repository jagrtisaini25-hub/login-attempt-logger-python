from datetime import datetime
import tkinter as tk
from tkinter import messagebox

# Users Database
users = {
    "admin": "12345",
    "hanny": "hanny123",
    "rahul": "rahul@123",
    "aman": "aman123"
}

attempt = 0
max_attempt = 3

# Login Function
def login():
    global attempt

    username = username_entry.get()
    password = password_entry.get()

    if username in users and password == users[username]:

        status = "SUCCESS"

        messagebox.showinfo("Login", f"Welcome {username}")

        with open("login_logs.txt", "a") as file:
            file.write(
                f"{datetime.now().strftime('%d-%m-%Y %I:%M:%S %p')} | Username: {username} | {status}\n"
            )

    else:

        attempt += 1
        status = "FAILED"

        with open("login_logs.txt", "a") as file:
            file.write(
                f"{datetime.now().strftime('%d-%m-%Y %I:%M:%S %p')} | Username: {username} | {status}\n"
            )

        if attempt == max_attempt:
            messagebox.showerror("Login", "Account Locked!")
            root.destroy()
        else:
            messagebox.showerror(
                "Login",
                f"Invalid Username or Password!\nAttempts Left: {max_attempt-attempt}"
            )

# GUI
root = tk.Tk()
root.title("Secure Login Attempt Logger")
root.geometry("350x220")

tk.Label(root, text="Username").pack(pady=5)
username_entry = tk.Entry(root)
username_entry.pack()

tk.Label(root, text="Password").pack(pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.pack()

tk.Button(root, text="Login", command=login, width=15).pack(pady=20)

root.mainloop()