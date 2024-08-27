import tkinter as tk
from tkinter import messagebox
import mysql.connector
from conexao import conectar_banco  # Importa a função de conexão do arquivo conexao.py

def registrar_produto(nome, categoria, preco, estoque):
    """Registra um novo produto no banco de dados."""
    try:
        conn = conectar_banco()  # Usa a função conectar_banco do arquivo conexao.py para conectar ao banco
        cursor = conn.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS products
                          (nome VARCHAR(255), categoria VARCHAR(255), preco DECIMAL(10, 2), estoque INT)''')

        cursor.execute("INSERT INTO products (nome, categoria, preco, estoque) VALUES (%s, %s, %s, %s)",
                       (nome, categoria, float(preco), int(estoque)))

        conn.commit()
        messagebox.showinfo("Cadastro de Produto", "Produto cadastrado com sucesso!")
    except mysql.connector.Error as err:
        messagebox.showerror("Erro", f"Algo deu errado: {err}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def abrir_janela_cadastro_produto():
    """Abre a janela de cadastro de produtos."""
    janela_cadastro_produto = tk.Toplevel()
    janela_cadastro_produto.title("Cadastro de Produtos")
    janela_cadastro_produto.geometry("400x250")

    tk.Label(janela_cadastro_produto, text="Nome do Produto").grid(row=0, column=0)
    tk.Label(janela_cadastro_produto, text="Categoria").grid(row=1, column=0)
    tk.Label(janela_cadastro_produto, text="Preço").grid(row=2, column=0)
    tk.Label(janela_cadastro_produto, text="Quantidade em Estoque").grid(row=3, column=0)

    entrada_nome = tk.Entry(janela_cadastro_produto)
    entrada_categoria = tk.Entry(janela_cadastro_produto)
    entrada_preco = tk.Entry(janela_cadastro_produto)
    entrada_estoque = tk.Entry(janela_cadastro_produto)

    entrada_nome.grid(row=0, column=1)
    entrada_categoria.grid(row=1, column=1)
    entrada_preco.grid(row=2, column=1)
    entrada_estoque.grid(row=3, column=1)

    botao_cadastrar_produto = tk.Button(janela_cadastro_produto, text="Cadastrar Produto", command=lambda: registrar_produto(
        entrada_nome.get(),
        entrada_categoria.get(),
        entrada_preco.get(),
        entrada_estoque.get()
    ))
    botao_cadastrar_produto.grid(columnspan=2)
