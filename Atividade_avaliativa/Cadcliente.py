from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
from BDCliente import Cliente, populate_treeview
from BDCidade import cidade, populate_treeview

class Application:
    def __init__(self, root):
        self.cliente = Cliente()  # Instancia a classe Cliente
        self.cidade = cidade()    # Instancia a classe Cidade

        self.root = root
        self.root.title("Cadastro de Clientes")
        self.root.configure(bg="#81c784")  # Define a cor de fundo da janela principal

        # Estilo dos botões
        estilo_botao = {
            "font": ("Times", 12),
            "bg": "#a5d6a7",
            "fg": "#1b5e20",
            "relief": "raised",
            "activebackground": "#1b5e20",
            "activeforeground": "#f0f0f0"
        }

        # Widgets
        self.lblIdCliente = Label(root, text="ID do Cliente:", bg="#81c784", fg="#1b5e20")
        self.lblIdCliente.grid(row=0, column=0)
        self.txtIdCliente = Entry(root)
        self.txtIdCliente.grid(row=0, column=1)

        self.btnBuscar = Button(root, text="Buscar", command=self.buscar_cliente, **estilo_botao)
        self.btnBuscar.grid(row=0, column=3)

        self.lblNome = Label(root, text="Nome:", bg="#81c784", fg="#1b5e20")
        self.lblNome.grid(row=1, column=0)
        self.txtNome = Entry(root)
        self.txtNome.grid(row=1, column=1)

        self.lblTelefone = Label(root, text="Telefone:", bg="#81c784", fg="#1b5e20")
        self.lblTelefone.grid(row=2, column=0)
        self.txtTelefone = Entry(root)
        self.txtTelefone.grid(row=2, column=1)

        self.lblEmail = Label(root, text="E-mail:", bg="#81c784", fg="#1b5e20")
        self.lblEmail.grid(row=3, column=0)
        self.txtEmail = Entry(root)
        self.txtEmail.grid(row=3, column=1)

        self.lblcidade = Label(root, text="Cidade:", bg="#81c784", fg="#1b5e20")
        self.lblcidade.grid(row=4, column=0)

        # Dropdown para cidades
        self.varcidade = StringVar(root)
        self.cidade_disponiveis = self.cidade.listar_cidades()
        if self.cidade_disponiveis:
            self.varcidade.set(self.cidade_disponiveis[0])  # Define a primeira cidade como padrão
        else:
            self.varcidade.set("")  # Caso não haja cidades, deixa o dropdown vazio

        self.dropdowncidade = OptionMenu(root, self.varcidade, *self.cidade_disponiveis)
        self.dropdowncidade.config(bg="#a5d6a7", fg="#1b5e20", activebackground="#1b5e20", activeforeground="#f0f0f0")
        self.dropdowncidade.grid(row=4, column=1)
         
        # Botões
        self.btnInserir = Button(root, text="Inserir", command=self.inserir_cliente, **estilo_botao)
        self.btnInserir.grid(row=5, column=0)

        self.btnAlterar = Button(root, text="Alterar", command=self.alterar_cliente, **estilo_botao)
        self.btnAlterar.grid(row=5, column=1)

        self.btnExcluir = Button(root, text="Excluir", command=self.excluir_cliente, **estilo_botao)
        self.btnExcluir.grid(row=5, column=2)

        self.btnVoltar = Button(root, text="Voltar", command=self.Principal, **estilo_botao)
        self.btnVoltar.grid(row=5, column=3, padx=6, pady=6)

        # Configurando o Treeview
        self.columns = ('ID CLIENTE', 'NOME', 'TELEFONE', 'EMAIL', 'ID CIDADE')
        self.treeview = ttk.Treeview(root, columns=self.columns, show="headings")
        for col in self.columns:
            self.treeview.heading(col, text=col)
        self.treeview.grid(row=8, column=0, columnspan=3, sticky="nsew")

        # Bind para detectar a seleção de um item no Treeview
        self.treeview.bind("<ButtonRelease-1>", self.selecionar_item_treeview)

        # Chama o método de refresh ao iniciar
        self.refresh_treeview()

        # Bind para detectar o fechamento da janela
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def refresh_treeview(self):
        """Função para atualizar o Treeview com os dados mais recentes."""
        data = self.cliente.listar_todos()
        # Limpa os dados antigos
        for row in self.treeview.get_children():
            self.treeview.delete(row)
        # Popula os novos dados
        for cliente in data:
            self.treeview.insert('', 'end', values=cliente)

    def selecionar_item_treeview(self, event):
        """Função para preencher os campos ao clicar em um item do Treeview."""
        selecionado = self.treeview.focus()
        valores = self.treeview.item(selecionado, 'values')
        
        if valores:
            self.txtIdCliente.delete(0, END)
            self.txtIdCliente.insert(END, valores[0])
            self.txtNome.delete(0, END)
            self.txtNome.insert(END, valores[1])
            self.txtTelefone.delete(0, END)
            self.txtTelefone.insert(END, valores[2])
            self.txtEmail.delete(0, END)
            self.txtEmail.insert(END, valores[3])
            self.varcidade.set(valores[4])

    def Principal(self):
        self.root.destroy()
        caminho_script = 'python Principal.py'
        os.system(caminho_script)

    def buscar_cliente(self):
        idCliente = self.txtIdCliente.get()
        if not idCliente:
            messagebox.showerror("Erro", "ID do cliente não pode estar vazio!")
            return

        resultado = self.cliente.buscar(idCliente)
        if resultado:
            self.txtNome.delete(0, END)
            self.txtNome.insert(END, resultado[1])
            self.txtTelefone.delete(0, END)
            self.txtTelefone.insert(END, resultado[2])
            self.txtEmail.delete(0, END)
            self.txtEmail.insert(END, resultado[3])
            if resultado[4] in self.cidade_disponiveis:
                self.varcidade.set(resultado[4])
            messagebox.showinfo("Sucesso", "Busca realizada com sucesso!")
        else:
            messagebox.showerror("Erro", "Cliente não encontrado!")
        self.refresh_treeview()

    def inserir_cliente(self):
        nome = self.txtNome.get()
        telefone = self.txtTelefone.get()
        email = self.txtEmail.get()
        cidade = self.varcidade.get()

        if not nome or not telefone or not email or not cidade:
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos!")
            return

        self.cliente.inserir(nome, telefone, email, cidade)
        messagebox.showinfo("Sucesso", "Cliente inserido com sucesso!")
        self.refresh_treeview()

    def alterar_cliente(self):
        idCliente = self.txtIdCliente.get()
        nome = self.txtNome.get()
        telefone = self.txtTelefone.get()
        email = self.txtEmail.get()
        cidade = self.varcidade.get()

        if not idCliente:
            messagebox.showerror("Erro", "ID do cliente não pode estar vazio!")
            return

        self.cliente.alterar(idCliente, nome, telefone, email, cidade)
        messagebox.showinfo("Sucesso", "Cliente alterado com sucesso!")
        self.refresh_treeview()

    def excluir_cliente(self):
        idCliente = self.txtIdCliente.get()
        if not idCliente:
            messagebox.showerror("Erro", "ID do cliente não pode estar vazio!")
            return

        self.cliente.excluir(idCliente)
        messagebox.showinfo("Sucesso", "Cliente excluído com sucesso!")
        self.refresh_treeview()

    def on_closing(self):
        if messagebox.askokcancel("Sair", "Você deseja sair do aplicativo?"):
            self.root.destroy()

# Execução da interface
if __name__ == "__main__":
    root = Tk()
    app = Application(root)
    root.state("zoomed")
    root.mainloop()
