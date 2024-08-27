import tkinter as tk
from tkinter import messagebox
from conexao import conectar_banco
from janela_venda import PDVApp

def fazer_login(usuario, senha):
    """Verifica as credenciais de login no banco de dados."""
    try:
        conn = conectar_banco()  # Usa a função conectar_banco do arquivo conexao.py para conectar ao banco
        cursor = conn.cursor()

        # Consulta o banco de dados para verificar as credenciais
        cursor.execute("SELECT * FROM usuarios WHERE usuario = %s AND senha = %s", (usuario, senha))
        resultado = cursor.fetchone()

        if resultado:
            messagebox.showinfo("Login", "Acesso permitido")
            abrir_janela_venda()
        else:
            messagebox.showerror("Login", "Acesso negado")
    except mysql.connector.Error as err:
        messagebox.showerror("Erro", f"Algo deu errado: {err}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def abrir_janela_venda():
    """Abre a janela de vendas."""
    janela_venda = tk.Toplevel()
    PDVApp(janela_venda)  # Cria uma instância da classe PDVApp, passando a janela de vendas

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
