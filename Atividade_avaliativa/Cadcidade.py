from tkinter import *  # Importa tudo do módulo tkinter
from tkinter import ttk
from tkinter import messagebox
import os
from BDCidade import cidade, populate_treeview  # Importa a classe cidade do módulo BDcidade

class Application:
    def __init__(self, root):
        self.cidade = cidade()

        self.root = root
        self.root.title("Cadastro de Cidades")
        self.root.configure(bg="#81c784")  # Cor de fundo da janela principal

        # Configuração dos Widgets
        self.lblIdcidade = Label(root, text="ID da Cidade:", font=("Times", 16), bg="#81c784", fg="#1b5e20")
        self.lblIdcidade.grid(row=0, column=0, padx=10, pady=5, sticky=E)
        self.txtIdcidade = Entry(root, font=("Times", 14), relief="flat")
        self.txtIdcidade.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        self.btnBuscar = Button(root, text="Buscar", font=("Times", 12), bg="#a5d6a7", fg="white", relief="raised",
                                activebackground="#1b5e20", activeforeground="white", command=self.buscar_cidade)
        self.btnBuscar.grid(row=0, column=2, padx=10, pady=5)

        self.lblNome = Label(root, text="Nome:", font=("Times", 16), bg="#81c784", fg="#1b5e20")
        self.lblNome.grid(row=1, column=0, padx=10, pady=5, sticky=E)
        self.txtNome = Entry(root, font=("Times", 14), relief="flat")
        self.txtNome.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        self.lblUf = Label(root, text="UF:", font=("Times", 16), bg="#81c784", fg="#1b5e20")
        self.lblUf.grid(row=2, column=0, padx=10, pady=5, sticky=E)
        self.txtUf = Entry(root, font=("Times", 14), relief="flat")
        self.txtUf.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # Botões
        self.btnInserir = Button(root, text="Inserir", font=("Times", 12), bg="#a5d6a7", fg="white", relief="raised",
                                 activebackground="#1b5e20", activeforeground="white", command=self.inserir_cidade)
        self.btnInserir.grid(row=3, column=0, padx=6, pady=6)

        self.btnAlterar = Button(root, text="Alterar", font=("Times", 12), bg="#a5d6a7", fg="white", relief="raised",
                                 activebackground="#1b5e20", activeforeground="white", command=self.alterar_cidade)
        self.btnAlterar.grid(row=3, column=1, padx=6, pady=6)

        self.btnExcluir = Button(root, text="Excluir", font=("Times", 12), bg="#a5d6a7", fg="white", relief="raised",
                                 activebackground="#1b5e20", activeforeground="white", command=self.excluir_cidade)
        self.btnExcluir.grid(row=3, column=2, padx=6, pady=6)

        self.btnVoltar = Button(root, text="Voltar", font=("Times", 12), bg="#a5d6a7", fg="white", relief="raised",
                                activebackground="#1b5e20", activeforeground="white", command=self.Principal)
        self.btnVoltar.grid(row=3, column=3, padx=6, pady=6)

        # Configurando o Treeview
        self.columns = ('ID', 'NOME CIDADE', 'UF')
        self.treeview = ttk.Treeview(root, columns=self.columns, show="headings")
        for col in self.columns:
            self.treeview.heading(col, text=col)
        self.treeview.grid(row=8, column=0, columnspan=4, sticky="nsew")

        # Chama o método de refresh ao iniciar
        self.refresh_treeview()

    def refresh_treeview(self):
        """Função para atualizar o Treeview com os dados mais recentes."""
        data = self.cidade.listar_cidades()  # Corrigido para usar self.cidade.listar_cidades()
        if not data:
         print("Nenhum dado encontrado ou ocorreu um erro ao buscar os dados.")
        else:
            populate_treeview(self.treeview, data)

    # Bind para detectar o fechamento da janela
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def Principal(self):
        self.root.destroy()
        caminho_script = 'python Principal.py'
        os.system(caminho_script)

    def buscar_cidade(self):
        idCidade = self.txtIdcidade.get()
        resultado = self.cidade.buscar(idCidade)
        if resultado:
            self.txtNome.delete(0, END)
            self.txtNome.insert(END, resultado[1])
            self.txtUf.delete(0, END)
            self.txtUf.insert(END, resultado[2])
            messagebox.showinfo("Busca Realizada", "Busca realizada com sucesso!")
        else:
            messagebox.showerror("Erro", "Cidade não encontrada!")
        self.refresh_treeview()

    def inserir_cidade(self):
        nome = self.txtNome.get()
        uf = self.txtUf.get()
        if nome and uf:
            self.cidade.inserir(nome, uf)
            messagebox.showinfo("Sucesso", "Cidade inserida com sucesso!")
        else:
            messagebox.showwarning("Aviso", "Nome e UF devem ser preenchidos.")
        self.refresh_treeview()

    def alterar_cidade(self):
        idCidade = self.txtIdcidade.get()
        nome = self.txtNome.get()
        uf = self.txtUf.get()
        if idCidade and nome and uf:
            self.cidade.alterar(idCidade, nome, uf)
            messagebox.showinfo("Sucesso", "Cidade alterada com sucesso!")
        else:
            messagebox.showwarning("Aviso", "ID da Cidade, Nome e UF devem ser preenchidos.")
        self.refresh_treeview()

    def excluir_cidade(self):
        idCidade = self.txtIdcidade.get()
        if idCidade:
            self.cidade.excluir(idCidade)
            messagebox.showinfo("Sucesso", "Cidade excluída com sucesso!")
        else:
            messagebox.showwarning("Aviso", "ID da Cidade deve ser preenchido.")
        self.refresh_treeview()

    def on_closing(self):
        self.root.destroy()
        os.system('python principal.py')  # Reabre o principal.py ao fechar a janela

# Execução da interface
if __name__ == "__main__":
    root = Tk()
    app = Application(root)
    root.state("zoomed")
    root.mainloop()
