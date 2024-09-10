from Banco import Banco

def populate_treeview(treeview, data):
    # Primeiro, limpe qualquer dado existente no Treeview
    for item in treeview.get_children():
        treeview.delete(item)

    # Agora, insira os novos dados
    for row in data:
        treeview.insert("", "end", values=row)

class Usuario:
    def __init__(self):
        self.banco = Banco()

    def inserir(self, nome, telefone, email, usuario, senha):
        cursor = self.banco.conexao.cursor()
        cursor.execute('''
            INSERT INTO usuarios (nome, telefone, email, usuario, senha)
            VALUES (?, ?, ?, ?, ?)
        ''', (nome, telefone, email, usuario, senha))
        self.banco.conexao.commit()

    def alterar(self, idUsuario, nome, telefone, email, usuario, senha):
        cursor = self.banco.conexao.cursor()
        cursor.execute('''
            UPDATE usuarios SET nome=?, telefone=?, email=?, usuario=?, senha=?
            WHERE idUsuario=?
        ''', (nome, telefone, email, usuario, senha, idUsuario))
        self.banco.conexao.commit()

    def excluir(self, idUsuario):
        cursor = self.banco.conexao.cursor()
        cursor.execute('DELETE FROM usuarios WHERE idUsuario=?', (idUsuario,))
        self.banco.conexao.commit()

    def buscar(self, idUsuario):
        cursor = self.banco.conexao.cursor()
        cursor.execute('SELECT * FROM usuarios WHERE idUsuario=?', (idUsuario,))
        return cursor.fetchone()

    def listar(self):
        cursor = self.banco.conexao.cursor()
        cursor.execute('SELECT idUsuario, nome, telefone, email FROM usuarios')
        return cursor.fetchall()
