class produto:
    """Representa um produto com nome, código e preço."""

    def __init__(self,nome,codigo,preco):
        """Inicializa os atributos do produto."""
        self.nome="irdratante"
        self.codigo=278327392
        self.preco="R$12.40"

    def exibir_detalhes(selrf):
        """Método para exibir os detalhes do produto."""
        return f"Produto:{selrf.nome}|Código:{selrf.codigo}|Preço:R${selrf}"
    
#Exemplo de uso:
produto1=produto("Notebook","E123",4500.00)
print(produto1.exibir_detalhes())

import sqlite3

#1.Conectar ao bonco de dados (se não existir, ele será criado)
#O arquivo do banco de dados será chamado 'estoque.db'
conn=squite3.connect('estoque.db')
print("conexão com o banco de dados estabelecida.")

#2.Criar um objeto cursor para executar comandos SQL
curso=conn.cursor()

#3.Definir o comando SQL para criar a tabela de produtos
#Utilizamos IF NOT EXISTS para evitar erros caso a tabela já exista

import pandas as pd

#Dados dos produtos em um dicionário
produto_dados={
    'ID'=[1,2,3],
    'Nome'=['Irdratanter','cremer','maquiagem'],
    'Preco'=[1200.00,150.00,300.00]
}

#Criando um DataFrame(tabela)
df=pd.DataFrame(produto_dados)

#Exibindo a tabela
print(df)

import sqlite3

#1.Conectar ao banco de banco de dados(se não existir, ele será criado)
#O arquivo do banco de dados será chamado 'meu_banco.db'
conn=sqlite3.connect('estoque.db')

#2.Criar um objeto cursor para executar comandos SQL
curso=conn.cursor()

#3.Criar uma tabela (se ainda não existir)
#O comando SQL é passado como uma string
curso.execute("""
CREATE TABLE IF NOT EXISTS usuarios(
    id ANTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
    idade INTEGER NOT NULL
)
""")

#4.Inserir alguns dados de exemplo(opcional)
curso.execute("")