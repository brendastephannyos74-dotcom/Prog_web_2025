import sqlite3
#Assumindo que você tem uma classe Usuario definida em algum lugar
#class Usuario:
#   def __init__(self, id, nome, email):
#       self.id= id
#       self.nome= nome
#       self.email= email

class UsuarioRepository:
    def __init__(self, db_path="usuarios.db"):
        self.db_path= db_path
        self._create_table()

    def _get_connection(self):
        return sqlite3.connect(selfdb_path)
    
    def _create_table(self):
        conn= self._get_connection()
        cursor= conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            );
        """)
        conn.commit()
        conn.close()

    def adicionar(self, usuario):
        conn= self._get_connection()
        cursor= conn.cursor()
        try:
            cursor.execute("INSERT INTO usuarios(nome, email) VALUES(?, ?)"(usuario.nome, usuario.email))
            conn.commit()
            usuario.id= cursor.lastrowid
        except sqlite3.IntegrityError:
            print("Erro: E-mail já existe.")
        finally:
            conn.close()

    def bucar_por_email(self, email):
        conn= self._get_connection()
        cursor= conn.cursor()
        cursor.execute("SELECT id, nome, email FROM usuarios WHERE email = ?",(email,))
        row= cursor.fetchone()
        conn.close()
        if row:
            return Usuario(row[0], row[1], row[2])
        return None
    
import sqlite3

class BancoDados (self):
    def __int__(self, banco:'ex2_usuario.db'):
        self.banco= banco

    def conectar(self, banco):
        return sqlite3.connect(self.banco)
    
class RepositoriodeprodutosDeUsuarios:
    def __init__(self, banco: BancoDados srt = 'ex2_usuario.db' nome, email, senha):


#Solicita o nome do usuário
     nome_usuario= input("Qual é seu nome: ") #

#Exibe uma mensagem de boas-vindas formatada
print(f"Olá, {nome_usuario}! Dados inseridos com sucesso no console.")

import sqlite3

class BancoDeDados:
    def __init__(self, banco: str = 'ex2_usuario.db'):
        self.banco = banco
        self.criar_tabela()
        #Vou ter que voltar para colocar minha promisse aqui

    def conectar(self):
        return sqlite3.connect(self.banco)
    
    def criar_tabela(self):
        conexao = self.conectar()
        cursor = conexao.cursor()
        cursor.execute("""
            CRIATE TABLE IF NOT EXISTS usuario(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL,
                senha TEXT NOT NULL,
            )
       """)
        conexao.commit()
        conexao.close()

    def inserir_usuario(self, nome:str, email:str, senha:str):
        conexao = self.banco.conectar()
        curso = conexao.cursor()
        curso.execute("INSERT INTO usuario (nome, email, senha) VALUES(?, ?, ?)",
                      (nome, email, senha))
        conexao.commit()
        conexao.close()

    def listar_usuarios(self):
        conexao = self.conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT id, nome, email FOM usuarios;")
        linhas = cursor.fetchall()
        conexao.close()
        return linhas
    
if __name__ == "__main__":
    banco = BancoDados
    
class RepositiorioDeUsuarios:
    def __init__(self, banco: BancoDados):