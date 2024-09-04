import sqlite3

class Banco:
    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        self.criar_tabela()

    def criar_tabela(self):
        cursor = self.conexao.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                idUsuario INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                telefone TEXT,
                email TEXT,
                usuario TEXT,
                senha TEXT
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS cidade (
                idcid INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                uf TEXT
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS cliente (
                idcli INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                telefone TEXT,
                email TEXT,
                idcid INTEGER,
                FOREIGN KEY (idcid) REFERENCES cidade(idcid)
            )
        ''')
        self.conexao.commit()

    def fechar_conexao(self):
        self.conexao.close()
