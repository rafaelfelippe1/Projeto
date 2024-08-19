import tkinter as tk
from tkinter import messagebox
from cadastro_produto import abrir_janela_cadastro_produto

def fazer_login(usuario, senha):
    """Verifica as credenciais de login."""
    if usuario == "admin" and senha == "admin":
        messagebox.showinfo("Login", "Acesso permitido")
        abrir_janela_cadastro_produto()
    else:
        messagebox.showerror("Login", "Acesso negado")

def abrir_janela_login():
    """Abre a janela de login."""
    janela_login = tk.Toplevel()
    janela_login.title("Janela de Login")
    janela_login.geometry("300x150")

    tk.Label(janela_login, text="Usuário").grid(row=0, column=0)
    tk.Label(janela_login, text="Senha").grid(row=1, column=0)

    entrada_usuario = tk.Entry(janela_login)
    entrada_senha = tk.Entry(janela_login, show="*")
    entrada_usuario.grid(row=0, column=1)
    entrada_senha.grid(row=1, column=1)

    botao_login = tk.Button(janela_login, text="Login",
                            command=lambda: fazer_login(entrada_usuario.get(), entrada_senha.get()))
    botao_login.grid(columnspan=2)
