import tkinter as tk
from tkinter import messagebox, simpledialog

class Janela_Principal:
    def __init__(self, root):
        super().__init__()
        self.root = root
        self.root.title("Janela Principal")
        self.items = []
        self.total = 0

        # Botões de ação
        """aqui definimos os nomes e tamanhos dos botoes a serem inseridos na GUI
            e o que que cada um deles fazem atraves do comando 'self'."""
        self.btn_cadastrar_produto = tk.Button(self.root, text="Cadastro de produto", command=self.cadastrar_produto)
        self.btn_cadastrar_produto.pack(side=tk.LEFT, padx=10, pady=10)

        self.btn_cadastrar_cliente = tk.Button(self.root, text="Cadastro de cliente", command=self.cadastrar_cliente)
        self.btn_cadastrar_cliente.pack(side=tk.LEFT, padx=10)

        self.btn_cancelar_venda = tk.Button(self.root, text="Registro de Venda", command=self.cancelar_venda)
        self.btn_cancelar_venda.pack(side=tk.LEFT, padx=10, pady=10)

        self.btn_localizar = tk.Button(self.root, text="Localizar Venda", command=self.localizar_venda)
        self.btn_localizar.pack(side=tk.LEFT, padx=10, pady=10)


    def cadastrar_produto(self):
        """Abre a janela de vendas."""
        janela_principal = tk.Toplevel()
        Janela_Principal(janela_principal)  # Cria uma instância da classe PDVApp, passando a janela de vendas
        janela_principal.geometry("600x400")

    def cadastrar_cliente(self):
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

    def localizar_venda(self):
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

if __name__ == "__main__":
    root = tk.Tk()
    app = Janela_Principal(root)
    root.mainloop()

