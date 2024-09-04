from tkinter import *
from tkinter import messagebox
import sys
import os

# Funções para abrir outras janelas
def abrir_cadusuario():
    try:
        janela.destroy()
        os.system('python cadusuario.py')
    except Exception as e:
        messagebox.showerror(janela, text=f"Não foi possível abrir cadusuario.py: {str(e)}", fg="#d32f2f", bg="#e0f7e0")

def abrir_cadcidade():
    try:
        janela.destroy()
        os.system('python cadcidade.py')
    except Exception as e:
        messagebox.showerror(janela, text=f"Não foi possível abrir cadcidade.py: {str(e)}", fg="#d32f2f", bg="#e0f7e0")

def abrir_cadcliente():
    try:
        janela.destroy()
        os.system('python cadcliente.py')
    except Exception as e:
        messagebox.showerror(janela, text=f"Não foi possível abrir cadcliente.py: {str(e)}", fg="#d32f2f", bg="#e0f7e0")

def sair():
    sys.exit()

# Criação da janela principal
janela = Tk()
janela.title("Menu")
janela.configure(bg="#81c784")  # Define a cor de fundo da janela principal em um verde claro suave

# Título da janela
titulo = Label(janela, text="Menu", font=("Times", 24, "bold"), bg="#81c784", fg="#1b5e20")
titulo.pack(pady=20)

# Frame para agrupar botões
frame_botoes = Frame(janela, bg="#81c784")  # Define a cor de fundo do frame no mesmo tom
frame_botoes.pack()

# Botão Usuários
btn_usuarios = Button(frame_botoes, text="Usuários", font=("Times", 14), bg="#a5d6a7", fg="white", relief="raised", activebackground="#1b5e20", activeforeground="white", command=abrir_cadusuario)
btn_usuarios.grid(row=0, column=0, padx=6, pady=6)

# Botão Cidades
btn_cidades = Button(frame_botoes, text="Cidades", font=("Times", 14), bg="#a5d6a7", fg="white", relief="raised",activebackground="#1b5e20", activeforeground="white", command=abrir_cadcidade)
btn_cidades.grid(row=0, column=1, padx=6, pady=6)

# Botão Clientes
btn_clientes = Button(frame_botoes, text="Clientes", font=("Times", 14), bg="#a5d6a7", fg="white", relief="raised",activebackground="#1b5e20", activeforeground="white", command=abrir_cadcliente)
btn_clientes.grid(row=0, column=2, padx=6, pady=6)

# Botão Sair
btn_sair = Button(frame_botoes, text="Sair", font=("Times", 14), bg="#a5d6a7", fg="white", relief="raised", activebackground="#1b5e20", activeforeground="white", command=sair)
btn_sair.grid(row=1, column=1, padx=6, pady=6)

# Configurações finais da janela
if __name__ == "__main__":
    janela.state("zoomed")
    janela.mainloop()
