import tkinter as Tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

def exportar_para_pdf():
    with PdfPages(pdf_file) as pdf:
        fig, ax = plt.subplots()
        as.plot([1, 2, 3, 4], [1, 4, 2, 3])
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title('Gráfico de Exemplo')
        pdf.savefig()
        plt.close()
    print("PDF exportado com sucesso.")

root = tk.Tk()
root.title("Exportar para PDF")
botao_exportar.pack()
root.mailoop()