import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("Janela de Login")
root.geometry("300x150")

tk.Label(root, text="Usuário").grid(row=0, column=2)
tk.Label(root, text="Senha").grid(row=1, column=2)

username_entry = tk.Entry(root)
password_entry = tk.Entry(root, show="*")
username_entry.grid(row=0, column=1)
password_entry.grid(row=1, column=1)

login_button = tk.Button(root, text="Login", command=lambda: login(username_entry.get(), password_entry.get()))
lost_button = tk.Button(root, text="Esqueci a Senha", command=lambda: print("Função esqueci a senha não implementada ainda"))
lost_button.grid(row=3, column=0, columnspan=2)
login_button.grid(columnspan=2)

def login(username, password):
    if username == "admin" and password == "admin":
        messagebox.showinfo("Login", "Acesso permitido")
    else:
        messagebox.showerror("Login", "Acesso negado")

root.mainloop()
