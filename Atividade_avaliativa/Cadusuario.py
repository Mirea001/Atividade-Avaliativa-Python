from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
from BDUsuario import Usuario, populate_treeview
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class Application:
    def __init__(self, root):
        self.usuario = Usuario()

        self.root = root
        self.root.title("Cadastro de Usuários")
        self.root.configure(bg="#81c784")

        self.lblIdUsuario = Label(root, text="idUsuario:", font=("Times", 16), bg="#81c784", fg="#1b5e20")
        self.lblIdUsuario.grid(row=0, column=0, padx=10, pady=10, sticky=W)
        self.txtIdUsuario = Entry(root)
        self.txtIdUsuario.grid(row=0, column=1, padx=10, pady=10)

        self.btnBuscar = Button(root, text="Buscar", font=("Times", 14), bg="#a5d6a7", fg="white", activebackground="#1b5e20", activeforeground="white", command=self.buscar_usuario)
        self.btnBuscar.grid(row=0, column=2, padx=6, pady=6)

        self.lblNome = Label(root, text="Nome:", font=("Times", 16), bg="#81c784", fg="#1b5e20")
        self.lblNome.grid(row=1, column=0, padx=10, pady=10, sticky=W)
        self.txtNome = Entry(root)
        self.txtNome.grid(row=1, column=1, padx=10, pady=10)

        self.lblTelefone = Label(root, text="Telefone:", font=("Times", 16), bg="#81c784", fg="#1b5e20")
        self.lblTelefone.grid(row=2, column=0, padx=10, pady=10, sticky=W)
        self.txtTelefone = Entry(root)
        self.txtTelefone.grid(row=2, column=1, padx=10, pady=10)

        self.lblEmail = Label(root, text="E-mail:", font=("Times", 16), bg="#81c784", fg="#1b5e20")
        self.lblEmail.grid(row=3, column=0, padx=10, pady=10, sticky=W)
        self.txtEmail = Entry(root)
        self.txtEmail.grid(row=3, column=1, padx=10, pady=10)

        self.lblUsuario = Label(root, text="Usuário:", font=("Times", 16), bg="#81c784", fg="#1b5e20")
        self.lblUsuario.grid(row=4, column=0, padx=10, pady=10, sticky=W)
        self.txtUsuario = Entry(root)
        self.txtUsuario.grid(row=4, column=1, padx=10, pady=10)

        self.lblSenha = Label(root, text="Senha:", font=("Times", 16), bg="#81c784", fg="#1b5e20")
        self.lblSenha.grid(row=5, column=0, padx=10, pady=10, sticky=W)
        self.txtSenha = Entry(root, show="*")
        self.txtSenha.grid(row=5, column=1, padx=10, pady=10)

        self.btnInserir = Button(root, text="Inserir", font=("Times", 14), bg="#a5d6a7", fg="#f0f0f0", activebackground="#1b5e20", activeforeground="#f0f0f0", command=self.inserir_usuario)
        self.btnInserir.grid(row=6, column=0, padx=6, pady=6)

        self.btnAlterar = Button(root, text="Alterar", font=("Times", 14), bg="#a5d6a7", fg="#f0f0f0", activebackground="#1b5e20", activeforeground="#f0f0f0", command=self.alterar_usuario)
        self.btnAlterar.grid(row=6, column=1, padx=6, pady=6)

        self.btnExcluir = Button(root, text="Excluir", font=("Times", 14), bg="#a5d6a7", fg="#f0f0f0", activebackground="#1b5e20", activeforeground="#f0f0f0", command=self.excluir_usuario)
        self.btnExcluir.grid(row=6, column=2, padx=6, pady=6)

        self.btnVoltar = Button(root, text="Voltar", font=("Times", 14), bg="#a5d6a7", fg="#f0f0f0", activebackground="#1b5e20", activeforeground="#f0f0f0", command=self.Principal)
        self.btnVoltar.grid(row=6, column=3, padx=6, pady=6)

        self.btnGerarPDF = Button(root, text="Gerar PDF", font=("Times", 14), bg="#a5d6a7", fg="#f0f0f0", activebackground="#1b5e20", activeforeground="#f0f0f0", command=self.gerar_pdf)
        self.btnGerarPDF.grid(row=6, column=4, padx=6, pady=6)

        self.columns = ('IDUSUÁRIO', 'NOME', 'TELEFONE', 'E-mail', 'USUÁRIO', 'SENHA')
        self.treeview = ttk.Treeview(root, columns=self.columns, show="headings")
        for col in self.columns:
            self.treeview.heading(col, text=col)
        self.treeview.grid(row=8, column=0, columnspan=4, sticky="nsew")

        self.refresh_treeview()

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def refresh_treeview(self):
        data = self.usuario.listar()
        if not data:
            print("Nenhum dado encontrado ou ocorreu um erro ao buscar os dados.")
        else:
            populate_treeview(self.treeview, data)

    def Principal(self):
        self.root.destroy()
        caminho_script = 'python Principal.py'
        os.system(caminho_script)

    def buscar_usuario(self):
        idUsuario = self.txtIdUsuario.get()
        if not idUsuario:
            messagebox.showerror("Erro", "ID do usuário não pode estar vazio!")
            return
        
        resultado = self.usuario.buscar(idUsuario)
        if resultado:
            self.txtNome.delete(0, END)
            self.txtNome.insert(END, resultado[1])
            self.txtTelefone.delete(0, END)
            self.txtTelefone.insert(END, resultado[2])
            self.txtEmail.delete(0, END)
            self.txtEmail.insert(END, resultado[3])
            self.txtUsuario.delete(0, END)
            self.txtUsuario.insert(END, resultado[4])
            self.txtSenha.delete(0, END)
            self.txtSenha.insert(END, resultado[5])
            messagebox.showinfo("Sucesso", "Busca realizada com sucesso!")
        else:
            messagebox.showerror("Erro", "Usuário não encontrado!")
        self.refresh_treeview()

    def inserir_usuario(self):
        nome = self.txtNome.get()
        telefone = self.txtTelefone.get()
        email = self.txtEmail.get()
        usuario = self.txtUsuario.get()
        senha = self.txtSenha.get()

        if not nome or not telefone or not email or not usuario or not senha:
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos!")
            return

        self.usuario.inserir(nome, telefone, email, usuario, senha)
        messagebox.showinfo("Sucesso", "Usuário inserido com sucesso!")
        self.refresh_treeview()

    def alterar_usuario(self):
        idUsuario = self.txtIdUsuario.get()
        nome = self.txtNome.get()
        telefone = self.txtTelefone.get()
        email = self.txtEmail.get()
        usuario = self.txtUsuario.get()
        senha = self.txtSenha.get()

        if not idUsuario:
            messagebox.showerror("Erro", "ID do usuário não pode estar vazio!")
            return

        self.usuario.alterar(idUsuario, nome, telefone, email, usuario, senha)
        messagebox.showinfo("Sucesso", "Usuário alterado com sucesso!")
        self.refresh_treeview()

    def excluir_usuario(self):
        idUsuario = self.txtIdUsuario.get()
        if not idUsuario:
            messagebox.showerror("Erro", "ID do usuário não pode estar vazio!")
            return

        self.usuario.excluir(idUsuario)
        messagebox.showinfo("Sucesso", "Usuário excluído com sucesso!")
        self.refresh_treeview()

    def gerar_pdf(self):
        if not self.treeview.get_children():
            messagebox.showerror("Erro", "Não há dados para gerar o PDF!")
            return

        resposta = messagebox.askyesno("Gerar PDF", "Deseja baixar o arquivo PDF com as informações?")
        if not resposta:
            return

        # Determina o caminho para a pasta Downloads do usuário
        caminho_downloads = os.path.join(os.path.expanduser("~"), "Downloads")
        nome_arquivo = os.path.join(caminho_downloads, "usuarios.pdf")

        c = canvas.Canvas(nome_arquivo, pagesize=letter)
        c.drawString(100, 750, "Lista de Usuários")

        y = 700
        for child in self.treeview.get_children():
            values = self.treeview.item(child)["values"]
            linha = f"ID: {values[0]}, Nome: {values[1]}, Telefone: {values[2]}, E-mail: {values[3]}, Usuário: {values[4]}"
            c.drawString(100, y, linha)
            y -= 20
            if y < 100:
                c.showPage()
                y = 750

        c.save()

        messagebox.showinfo("Sucesso", f"PDF gerado com sucesso em {nome_arquivo}!")

    def on_closing(self):
        if messagebox.askokcancel("Sair", "Você deseja sair?"):
            self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    app = Application(root)
    root.mainloop()
