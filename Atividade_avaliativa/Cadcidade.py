from tkinter import *  # Importa tudo do módulo tkinter
import os
from BDCidade import cidade  # Importa a classe cidade do módulo BDcidade

class Application:
    def __init__(self, root):
        self.cidade = cidade()

        self.root = root
        self.root.title("Cadastro de Cidades")
        self.root.configure(bg="#81c784")  # Cor de fundo da janela principal

        # Widgets
        self.lblIdcidade = Label(root, text="ID da Cidade:", font=("Times", 16), bg="#81c784", fg="#1b5e20")
        self.lblIdcidade.grid(row=0, column=0, padx=10, pady=5, sticky=E)
        self.txtIdcidade = Entry(root, font=("Times", 14), relief="flat")
        self.txtIdcidade.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        self.btnBuscar = Button(root, text="Buscar", font=("Times", 12), bg="#a5d6a7", fg="#1b5e20", relief="raised", activebackground="#1b5e20", activeforeground="#f0f0f0", command=self.buscar_cidade)
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
        self.btnInserir = Button(root, text="Inserir", font=("Times", 12), bg="#a5d6a7", fg="#1b5e20", relief="raised", activebackground="#1b5e20", activeforeground="#f0f0f0", command=self.inserir_cidade)
        self.btnInserir.grid(row=3, column=0, padx=6, pady=6)

        self.btnAlterar = Button(root, text="Alterar", font=("Times", 12), bg="#a5d6a7", fg="#1b5e20", relief="raised", activebackground="#1b5e20", activeforeground="#f0f0f0", command=self.alterar_cidade)
        self.btnAlterar.grid(row=3, column=1, padx=6, pady=6)

        self.btnExcluir = Button(root, text="Excluir", font=("Times", 12), bg="#a5d6a7", fg="#1b5e20", relief="raised", activebackground="#1b5e20", activeforeground="#f0f0f0", command=self.excluir_cidade)
        self.btnExcluir.grid(row=3, column=2, padx=6, pady=6)

        self.lblMensagem = Label(root, text="", font=("Times", 14), bg="#81c784", fg="#d32f2f")  # Mensagem de feedback
        self.lblMensagem.grid(row=4, column=0, columnspan=3, pady=10)

        # Bind para detectar o fechamento da janela
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def buscar_cidade(self):
        idCidade = self.txtIdcidade.get()
        resultado = self.cidade.buscar(idCidade)
        if resultado:
            self.txtNome.delete(0, END)
            self.txtNome.insert(END, resultado[1])
            self.txtUf.delete(0, END)
            self.txtUf.insert(END, resultado[2])
            self.lblMensagem.config(text="Busca realizada com sucesso!", fg="#388e3c")
        else:
            self.lblMensagem.config(text="Cidade não encontrada!", fg="#d32f2f")

    def inserir_cidade(self):
        nome = self.txtNome.get()
        uf = self.txtUf.get()
        self.cidade.inserir(nome, uf)
        self.lblMensagem.config(text="Cidade inserida com sucesso!", fg="#388e3c")

    def alterar_cidade(self):
        idCidade = self.txtIdcidade.get()
        nome = self.txtNome.get()
        uf = self.txtUf.get()
        self.cidade.alterar(idCidade, nome, uf)
        self.lblMensagem.config(text="Cidade alterada com sucesso!", fg="#388e3c")

    def excluir_cidade(self):
        idCidade = self.txtIdcidade.get()
        self.cidade.excluir(idCidade)
        self.lblMensagem.config(text="Cidade excluída com sucesso!", fg="#388e3c")

    def on_closing(self):
        self.root.destroy()
        os.system('python principal.py')  # Reabre o principal.py ao fechar a janela

# Execução da interface
if __name__ == "__main__":
    root = Tk()
    app = Application(root)
    root.state("zoomed")
    root.mainloop()
