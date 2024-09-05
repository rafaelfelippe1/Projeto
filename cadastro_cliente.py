import tkinter as tk
from tkinter import messagebox

def salvar_cliente():
    codigo = entry_codigo.get()
    nome = entry_nome.get()
    cpf = entry_cpf.get()
    email = entry_email.get()
    telefone = entry_telefone.get()
    endereco = entry_endereco.get()
    if nome and cpf and email and telefone and endereco and codigo:
        # falta por o insert para upar os dados pro banco
        messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
    else:
        messagebox.showwarning("Erro", "Preencha todos os campos!")

janela = tk.Tk()
janela.title("Cadastro de Cliente")

label_codigo = tk.Label(janela, text="Codigo de Cliente:")
label_codigo.grid(row=0, column=0, padx=10, pady=10)
entry_codigo = tk.Entry(janela)
entry_codigo.grid(row=0, column=1, padx=10, pady=10)

label_nome = tk.Label(janela, text="Nome:")
label_nome.grid(row=1, column=0, padx=10, pady=10)
entry_nome = tk.Entry(janela)
entry_nome.grid(row=1, column=1, padx=10, pady=10)

label_cpf = tk.Label(janela, text="CPF:")
label_cpf.grid(row=2, column=0, padx=10, pady=10)
entry_cpf = tk.Entry(janela)
entry_cpf.grid(row=2, column=1, padx=10, pady=10)

label_email = tk.Label(janela, text="E-mail:")
label_email.grid(row=3, column=0, padx=10, pady=10)
entry_email = tk.Entry(janela)
entry_email.grid(row=3, column=1, padx=10, pady=10)

label_telefone = tk.Label(janela, text="Telefone:")
label_telefone.grid(row=4, column=0, padx=10, pady=10)
entry_telefone = tk.Entry(janela)
entry_telefone.grid(row=4, column=1, padx=10, pady=10)


label_endereco = tk.Label(janela, text="Endereço:")
label_endereco.grid(row=5, column=0, padx=10, pady=10)
entry_endereco = tk.Entry(janela)
entry_endereco.grid(row=5, column=1, padx=10, pady=10)

btn_salvar = tk.Button(janela, text="Cadastrar Cliente", command=salvar_cliente)
btn_salvar.grid(row=6, column=1, padx=10, pady=10)

#falta definir a funcao do botao de salvar para salvar os dados inseridos dentro do banco

janela.mainloop()
