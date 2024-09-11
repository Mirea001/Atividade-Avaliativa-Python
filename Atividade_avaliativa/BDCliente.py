from Banco import Banco

def populate_treeview(treeview, data):
    # Primeiro, limpe qualquer dado existente no Treeview
    for item in treeview.get_children():
        treeview.delete(item)

    # Agora, insira os novos dados
    for row in data:
        treeview.insert("", "end", values=row)


class Cliente:
    def __init__(self):
        self.banco = Banco()

    def inserir(self, nome, telefone, email, cidade):
        cursor = self.banco.conexao.cursor()
        cursor.execute('''
            INSERT INTO cliente (nome, telefone, email, idcid)
            VALUES (?, ?, ?, ?)
        ''', (nome, telefone, email, cidade))
        self.banco.conexao.commit()

    def alterar(self, idcli, nome, telefone, email, cidade):
        cursor = self.banco.conexao.cursor()
        cursor.execute('''
            UPDATE cliente SET nome=?, telefone=?, email=?, idcid=?
            WHERE idcli=?
        ''', (nome, telefone, email, cidade, idcli))
        self.banco.conexao.commit()

    def excluir(self, idcli):
        cursor = self.banco.conexao.cursor()
        cursor.execute('DELETE FROM cliente WHERE idcli=?', (idcli,))
        self.banco.conexao.commit()

    def buscar(self, idcli):
        cursor = self.banco.conexao.cursor()
        cursor.execute('SELECT * FROM cliente WHERE idcli=?', (idcli,))
        return cursor.fetchone()
    def listar_todos(self):
        try:
            cursor = self.banco.conexao.cursor()
            cursor.execute("SELECT idcli, nome, telefone, email, idcid FROM cliente")  # Ajuste conforme o nome real da tabela
            clientes = cursor.fetchall()
            return clientes
        except Exception as e:
            print(f"Erro ao listar clientes: {e}")
            return []
