import tkinter as tk
from login import abrir_janela_login
from cadastro_usuario import abrir_janela_cadastro

# Configuração da janela principal
root = tk.Tk()
root.title("Login")
root.geometry("200x200")

# Botões na janela principal para abrir as janelas de login e cadastro
botao_login = tk.Button(root, text="Login", command=abrir_janela_login)
botao_cadastro = tk.Button(root, text="Cadastro", command=abrir_janela_cadastro)
botao_login.pack(pady=10)
botao_cadastro.pack()

# Inicia o loop principal da aplicação
root.mainloop()
