import tkinter as tk
from tkinter import messagebox


# Função para lidar com o processo de login
def login(username, password):
    """Verifica as credenciais de login.
    Se o usuário e a senha forem "admin", o acesso é permitido.
    Caso contrário, o acesso é negado."""
    if username == "admin" and password == "admin":
        messagebox.showinfo("Login", "Acesso permitido")
    else:
        messagebox.showerror("Login", "Acesso negado")


# Função para lidar com o processo de registro de um novo usuário
def register(full_name, username, password, confirm_password, email):
    """Realiza o registro de um novo usuário.
    Primeiro, verifica se as senhas inseridas coincidem.
    Se sim, mostra uma mensagem informando que o usuário foi cadastrado com sucesso...
    Se não, mostra uma mensagem de erro indicando que as senhas não coincidem."""
    if password != confirm_password:
        messagebox.showerror("Cadastro", "As senhas não coincidem.")
        return

    messagebox.showinfo("Cadastro", f"Usuário {username} cadastrado com sucesso!")


# Função para abrir a janela de login
def open_login_window():
    """Abre uma nova janela de login.
    nessa janela contém campos para inserir o usuário e a senha,
     com um botão para enviar essas informações à função de login."""
    login_window = tk.Toplevel(root)
    login_window.title("Janela de Login")
    login_window.geometry("300x150")

    tk.Label(login_window, text="Usuário").grid(row=0, column=0)
    tk.Label(login_window, text="Senha").grid(row=1, column=0)

    username_entry = tk.Entry(login_window)
    password_entry = tk.Entry(login_window, show="*")
    username_entry.grid(row=0, column=1)
    password_entry.grid(row=1, column=1)

    login_button = tk.Button(login_window, text="Login",
                             command=lambda: login(username_entry.get(), password_entry.get()))
    login_button.grid(columnspan=2)


# Função para abrir a janela de cadastro
def open_register_window():
    """Abre uma nova janela de cadastro de um novo usuário.
    Dentro dessa janela contém campos para inserir o nome completo, usuário, email e etc...
    com um botão para enviar essas informações à função de registro dentro do BD."""
    register_window = tk.Toplevel(root)
    register_window.title("Cadastro de Usuário")
    register_window.geometry("400x250")

    tk.Label(register_window, text="Nome Completo").grid(row=0, column=0)
    tk.Label(register_window, text="Usuário").grid(row=1, column=0)
    tk.Label(register_window, text="Email").grid(row=2, column=0)
    tk.Label(register_window, text="Senha").grid(row=3, column=0)
    tk.Label(register_window, text="Confirmar Senha").grid(row=4, column=0)

    full_name_entry = tk.Entry(register_window)
    username_entry = tk.Entry(register_window)
    email_entry = tk.Entry(register_window)
    password_entry = tk.Entry(register_window, show="*")
    confirm_password_entry = tk.Entry(register_window, show="*")

    full_name_entry.grid(row=0, column=1)
    username_entry.grid(row=1, column=1)
    email_entry.grid(row=2, column=1)
    password_entry.grid(row=3, column=1)
    confirm_password_entry.grid(row=4, column=1)

    register_button = tk.Button(register_window, text="Registrar", command=lambda: register(
        full_name_entry.get(),
        username_entry.get(),
        password_entry.get(),
        confirm_password_entry.get(),
        email_entry.get()
    ))
    register_button.grid(columnspan=2)


# Configuração da janela principal
root = tk.Tk()
root.title("TESTE")
root.geometry("300x100")

# Botões na janela principal para abrir as janelas de login e cadastro
login_button = tk.Button(root, text="Login", command=open_login_window)
register_button = tk.Button(root, text="Cadastro", command=open_register_window)
login_button.pack(pady=10)
register_button.pack()

# Inicia o loop principal da aplicação
root.mainloop()
