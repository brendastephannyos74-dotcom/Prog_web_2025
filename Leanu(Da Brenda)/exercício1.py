import sqlite3 #È um comando  python que carrega o módulo, permitindo que um programa python interaja com bancos de dados SQLite

class BancoDeDados: #Refere-se à definição de uma classe de programação orientada a objetos que representa uma tabela em um banco de dados

    def __init__(self, caminho_banco:str="ex1_produtos.db"): #Defina como "def" palavra-chave usada para definir uma função ou método, "__init__" este é um método espesial, também chamando de "método mágico"ou"construtor.Ele é invocado automaticamente sempre que uma nova instância (objeto) da classe é criada,"(self)"é o primeiro parâmetro de qualquer método em uma classe phython e refere-se à própria instância do objeto que está sendo criada,"caminnho_banco:str"define um parâmentro chamado 'caminho_banco' e indica, usando anotação de tipo 
        self.caminho_banco=caminho_banco

    def conectar(self):
        return sqlite3.connect(self.caminho_banco)
    
class RepositorioDeProdutos:

    def __init__(self, banco: BancoDeDados):
        self.banco=banco

    def criar_tabela(self):
        conexao=self.banco.conectar()
        cursor=conexao.cursor()
        comando_criacao="""
        CREATE TABLE IF NOT EXISTS produtos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            preco REAL
        );
        """
        cursor.execute(comando_criacao)
        conexao.commit()
        conexao.close()

if __name__ == "__main__":
    banco = BancoDeDados()
    repositorio=RepositorioDeProdutos(banco)

    repositorio.criar_tabela()
    print("Tabela criada com sucesso!")