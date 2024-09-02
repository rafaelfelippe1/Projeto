import tkinter as tk
from tkinter import messagebox
import mysql.connector
from conexao import conectar_banco  # Importa a função de conexão do arquivo conexao.py

def registrar_usuario(nome_completo, usuario, senha, confirmar_senha, email):
    """Realiza o registro de um novo usuário no banco de dados."""
    if senha != confirmar_senha:
        messagebox.showerror("Cadastro", "As senhas não coincidem.")
        return

    conn = None
    try:
        conn = conectar_banco()  # Usa a função conectar_banco do arquivo conexao.py para conectar ao banco
        cursor = conn.cursor()

        # Cria a tabela se não existir
        cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                          nome_completo VARCHAR(255),
                          usuario VARCHAR(255) UNIQUE,
                          senha VARCHAR(255),
                          email VARCHAR(255))''')

        # Insere os dados do usuário na tabela
        cursor.execute("INSERT INTO usuarios (nome_completo, usuario, senha, email) VALUES (%s, %s, %s, %s)",
                       (nome_completo, usuario, senha, email))

        conn.commit()  # Confirma as mudanças no banco de dados
        messagebox.showinfo("Cadastro", f"Usuário {usuario} cadastrado com sucesso!")
    except mysql.connector.Error as err:
        messagebox.showerror("Erro", f"Algo deu errado: {err}")
    finally:
        if conn is not None and conn.is_connected():
            cursor.close()
            conn.close()

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

