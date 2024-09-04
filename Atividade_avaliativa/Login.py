from tkinter import *
from tkinter import messagebox
from BDUsuario import Banco
import os

class Application:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.configure(bg="#81c784")

        # Carregar e exibir a imagem na parte superior
        self.img = PhotoImage(file="loginimagem.png")  # Substitua pelo caminho correto da imagem
        self.lblImagem = Label(root, image=self.img, bg="#81c784")
        self.lblImagem.grid(row=0, column=0, columnspan=2, pady=10)  # Colocando a imagem no topo

        self.lbllogin = Label(root, text="Usuário:", font=("Times", 16), bg="#81c784", fg="#1b5e20")
        self.lbllogin.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.txtlogin = Entry(root)
        self.txtlogin.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        self.lblSenha = Label(root, text="Senha:", font=("Times", 16), bg="#81c784", fg="#1b5e20")
        self.lblSenha.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.txtSenha = Entry(root, show="*")
        self.txtSenha.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        self.btnlogin = Button(root, text="Login", font=("Times", 14), bg="#a5d6a7", fg="#f0f0f0",
                               activebackground="#1b5e20", activeforeground="#f0f0f0", command=self.verificar_login)
        self.btnlogin.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
    
    def verificar_login(self):
        usuario = self.txtlogin.get()
        senha = self.txtSenha.get()
        
        banco_con = Banco()
        try:
            c = banco_con.conexao.cursor()
            c.execute("SELECT * FROM usuarios WHERE usuario = ? AND senha = ?", (usuario, senha))
            resultado = c.fetchone()
            c.close()
            
            if resultado:
                messagebox.showinfo("Verificado", "Login efetuado")
                self.abrir_principal()
            else:
                messagebox.showerror("Erro", "Usuário ou senha incorretos")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro na busca do usuário: {str(e)}")
        
    def abrir_principal(self):
        # Oculta a janela de login e abre o script Principal.py
        self.root.destroy()
        caminho_script = 'python Principal.py'
        os.system(caminho_script)

if __name__ == "__main__":
    root = Tk()
    app = Application(root)
    root.state('zoomed')
    root.mainloop()
