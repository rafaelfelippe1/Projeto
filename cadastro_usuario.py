import tkinter as tk
from tkinter import messagebox

def registrar_usuario(nome_completo, usuario, senha, confirmar_senha, email):
    """Realiza o registro de um novo usuário."""
    if senha != confirmar_senha:
        messagebox.showerror("Cadastro", "As senhas não coincidem.")
        return

    messagebox.showinfo("Cadastro", f"Usuário {usuario} cadastrado com sucesso!")

def abrir_janela_cadastro():
    """Abre a janela de cadastro de usuário."""
    janela_cadastro = tk.Toplevel()
    janela_cadastro.title("Cadastro de Usuário")
    janela_cadastro.geometry("400x250")

    tk.Label(janela_cadastro, text="Nome Completo").grid(row=0, column=0)
    tk.Label(janela_cadastro, text="Usuário").grid(row=1, column=0)
    tk.Label(janela_cadastro, text="Email").grid(row=2, column=0)
    tk.Label(janela_cadastro, text="Senha").grid(row=3, column=0)
    tk.Label(janela_cadastro, text="Confirmar Senha").grid(row=4, column=0)

    entrada_nome_completo = tk.Entry(janela_cadastro)
    entrada_usuario = tk.Entry(janela_cadastro)
    entrada_email = tk.Entry(janela_cadastro)
    entrada_senha = tk.Entry(janela_cadastro, show="*")
    entrada_confirmar_senha = tk.Entry(janela_cadastro, show="*")

    entrada_nome_completo.grid(row=0, column=1)
    entrada_usuario.grid(row=1, column=1)
    entrada_email.grid(row=2, column=1)
    entrada_senha.grid(row=3, column=1)
    entrada_confirmar_senha.grid(row=4, column=1)

    botao_cadastrar = tk.Button(janela_cadastro, text="Registrar", command=lambda: registrar_usuario(
        entrada_nome_completo.get(),
        entrada_usuario.get(),
        entrada_senha.get(),
        entrada_confirmar_senha.get(),
        entrada_email.get()
    ))
    botao_cadastrar.grid(columnspan=2)
