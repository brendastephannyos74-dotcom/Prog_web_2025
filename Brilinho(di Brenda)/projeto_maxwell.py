import sqlite3

def conectar(self):
    return sqlite3.connect(self.banco)

def criar_extintor(self):
    conexao= self.conectar()
    cursor= conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS extintores(
            id INTEGER PRIMAY KEY AUTOINCREMENT,
            tipo TEXT NOT NULL,
            data_verificacao TEXT NOT NULL
            local TEXT NOT NULL,
            validade TEXT NOT NULL
        );
    """)
    conexao.commit()
    conexao.close()

def editar_extindor(self, tipo, data_vefificacao. local, validade):
    conexao =self.conectar()
    cursor = conexao.cursor()
    cursor = execute("-------------")
    conexao.commit()
    conexao.close