import tkinter as tk
from tkinter import messagebox, simpledialog, ttk


class DialogoPersonalizado(tk.Toplevel):  #classe que cria uma caixa de dialogo personalizada
    def __init__(self, pai, titulo=None):
        super().__init__(pai)
        self.root = root

        if titulo:
            self.title(titulo)

        self.resultado = None

        tk.Label(self, text="Código do Item:").grid(row=0, column=0, sticky="e")
        self.codigo_entry = tk.Entry(self, width=40)
        self.codigo_entry.grid(row=0, column=1)

        tk.Label(self, text="Nome do Item:").grid(row=1, column=0, sticky="e")
        self.nome_entry = tk.Entry(self, width=40)
        self.nome_entry.grid(row=1, column=1)

        tk.Label(self, text="Unidade:").grid(row=2, column=0, sticky="e")
        self.unidade_entry = tk.Entry(self, width=40)
        self.unidade_entry.grid(row=2, column=1)

        tk.Label(self, text="Quantidade:").grid(row=3, column=0, sticky="e")
        self.quantidade_entry = tk.Entry(self, width=40)
        self.quantidade_entry.grid(row=3, column=1)

        tk.Label(self, text="Preço:").grid(row=4, column=0, sticky="e")
        self.preco_entry = tk.Entry(self, width=40)
        self.preco_entry.grid(row=4, column=1)

        self.ok_button = tk.Button(self, text="OK", command=self.on_ok)
        self.ok_button.grid(row=5, column=0, columnspan=2, pady=5)

        self.grab_set()
        self.transient(pai)
        self.wait_window(self)

    def on_ok(self):
        """definicão da acão ao pressionar o botão de ok,
         que recupera os dados inseridos e os guarda na lista de itens"""
        codigo = self.codigo_entry.get()
        """ repare que o 'get' é quem guarda os dados inseridos na linha"""
        nome = self.nome_entry.get()
        unidade = self.unidade_entry.get()
        quantidade = float(self.quantidade_entry.get())
        preco = float(self.preco_entry.get())
        total = quantidade * preco

        self.resultado = (codigo, nome, unidade, quantidade, preco, total)
        self.destroy()

class PDVApp:
    def __init__(self, root):
        super().__init__()
        self.root = root
        self.root.title("Sistema de Vendas")
        self.items = []
        self.total = 0

        self.items_frame = tk.Frame(self.root)
        self.items_frame.pack(fill=tk.BOTH, expand=True)

        self.columns = ("Código", "Nome", "Unidade", "Quantidade", "Preço", "Total")
        self.items_list = ttk.Treeview(self.items_frame, columns=self.columns, show="headings")
        for col in self.columns:
            self.items_list.heading(col, text=col)
            self.items_list.column(col, anchor=tk.CENTER)
        self.items_list.pack(fill=tk.BOTH, expand=True)

        # Tabela de itens
        """Aqui definimos a tabela onde serão mostrados os itens linha por linha.
           Podemos definir o tamanho da altura e da largura usando width e height."""
        self.lista_itens = tk.Listbox(self.root, width=95, height=20)
        self.lista_itens.pack()

        # Total da venda
        """A área do preço total é centralizada.
           Podemos definir a margem usando 'pady' e definir o tamanho da margem,
           e definir uma fonte e o tamanho da mesma dentro do parâmetro 'font', logo em seguida do texto a ser mostrado."""
        self.total_label = tk.Label(self.root, text="Total: R$ 0,00", font=("Arial", 16))
        self.total_label.pack(pady=10)

        # Botões de ação
        """aqui definimos os nomes e tamanhos dos botoes a serem inseridos na GUI
            e o que que cada um deles fazem atraves do comando 'self'."""
        self.btn_adicionar_item = tk.Button(self.root, text="Adicionar Item", command=self.adicionar_item)
        self.btn_adicionar_item.pack(side=tk.LEFT, padx=10, pady=10)

        self.btn_cancelar_item = tk.Button(self.root, text="Cancelar Item", command=self.cancelar_item)
        self.btn_cancelar_item.pack(side=tk.LEFT, padx=10)

        self.btn_cancelar_venda = tk.Button(self.root, text="Cancelar Venda", command=self.cancelar_venda)
        self.btn_cancelar_venda.pack(side=tk.LEFT, padx=10, pady=10)

        self.btn_localizar = tk.Button(self.root, text="Localizar Produto", command=self.localizar_produto)
        self.btn_localizar.pack(side=tk.LEFT, padx=10, pady=10)

        self.btn_pagamento = tk.Button(self.root, text="Selecionar Pagamento", command=self.metodo_pagamento)
        self.btn_pagamento.pack(side=tk.LEFT, padx=10, pady=10)

    def adicionar_item(self):
        dialogo = DialogoPersonalizado(self.root, "Adicionar Item")
        if dialogo.resultado:
            self.items.append(dialogo.resultado)
            self.atualizar_lista_itens()
            self.atualizar_total()

    def cancelar_item(self):
        selecionado = self.lista_itens.curselection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Nenhum item selecionado para cancelamento.")
            return

        indice = selecionado[0]
        del self.items[indice]
        self.atualizar_lista_itens()
        self.atualizar_total()

    def cancelar_venda(self):
        if messagebox.askyesno("Confirmar", "Tem certeza que deseja cancelar a venda?"):
            self.items = []
            self.atualizar_lista_itens()
            self.atualizar_total()

    def localizar_produto(self):
        termo_busca = simpledialog.askstring("Buscar Produto", "Digite o nome do produto:")
        itens_encontrados = [item for item in self.items if termo_busca.lower() in item[1].lower()]
        if itens_encontrados:
            self.resultado_busca(itens_encontrados)
        else:
            messagebox.showinfo("Resultado", "Nenhum produto encontrado.")

    def resultado_busca(self, itens_encontrados):
        janela_resultados = tk.Toplevel(self.root)
        janela_resultados.title("Resultados da Busca")

        lista_resultados = tk.Listbox(janela_resultados, width=95, height=10)
        lista_resultados.pack()

        for item in itens_encontrados:
            lista_resultados.insert(tk.END, f"Código: {item[0]}, Nome: {item[1]}, Unidade: {item[2]}, "
                                            f"Quantidade: {item[3]}, Preço: R$ {item[4]:.2f}, Total: R$ {item[5]:.2f}")

    def metodo_pagamento(self):
        formas_pagamento = ["Dinheiro", "Cartão de Crédito", "Cartão de Débito", "Pix"]
        forma_pagamento = simpledialog.askstring("Forma de Pagamento",
                                                 "Escolha a forma de pagamento:\n" + "\n".join(formas_pagamento))
        if forma_pagamento in formas_pagamento:
            messagebox.showinfo("Pagamento", f"Forma de pagamento selecionada: {forma_pagamento}")
        else:
            messagebox.showwarning("Aviso", "Forma de pagamento inválida.")

    def atualizar_lista_itens(self):
        self.lista_itens.delete(0, tk.END)
        for item in self.items:
            self.lista_itens.insert(tk.END, f"Código: {item[0]}, Nome: {item[1]}, Unidade: {item[2]}, "
                                            f"Quantidade: {item[3]}, Preço: R$ {item[4]:.2f}, Total: R$ {item[5]:.2f}")

    def atualizar_total(self):
        self.total = sum(item[5] for item in self.items)
        self.total_label.config(text=f"Total: R$ {self.total:.2f}")


if __name__ == "__main__":
    root = tk.Tk()
    app = PDVApp(root)
    root.mainloop()

