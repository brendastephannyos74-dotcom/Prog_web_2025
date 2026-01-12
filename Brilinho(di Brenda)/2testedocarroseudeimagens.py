class Produtos:
    """Repredenta um produto com estoque."""
    def __init__(self, id_produto, nome, preco, quantidade_estoque):
        self.id_produto = id_produto
        self.nome = nome
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque

    def vender(self, quantidade):
        """Tenta vender uma quantidade do produto."""
        if quantidade <= self.quantidade_estoque:
            self.quantidade_estoque -= quantidade
            print(f"Venda de {quantidade} unidades de '{self.nome}'. realizada com sucesso.")
            return True
        else:
            print(f"Erro: Estoque insuficiente para '{self.nome}'. Estoque atual:{self.quantidade_estoque}.")
            return False
        
    def __str__(self):
        """Representação em string do produto."""
        return f"ID: {self.id_produto}|Nome:{self.nome}|Preço:R${self.preco:.2f}|Estoque:{self.quantidade_estoque}"
    
class SistemaVendas:
    """Gerencia os produtos e as vendas."""
    def __init__(self):
        #Dicionário para armazenar produtos, usando o ID como chave
        self.produtos = {}

    def adicionar_produto(self, produto):
        """Adiciona um novo produto ao sistema."""
        self.produtos[produ.id_produto]=produto
        print(f"Produto '{produto.nome}' adicionado.")

    def lista_produtos(self):
        """Lista todos os produtos disponíveis."""
        print("\n--- Produtos em Estoque ---")
        for produto in self.produtos.values():
            print(produto)
        print("----------------------------")

    def realizar_venda(self, id_produto, quantidade):
        """Processa uma operação de venda."""
        if id_produto in self.produtos:
            Produto = self.produtos[id_produto]
            if Produto.vender(quantidade):
                print(f"Total da vende: R${quantidade * Produto.preco:.2f}")
        elif:
            print (f"Erro: Produto com ID {id_produto} não encontrado.")

# --- Exemplo de Uso ---
if __name__ == "__main__":
    sistema = SistemaVendas()

    # Adicionando alguns produtos
    p1 = Produtos(id_produto=1, nome="Camiseta PYthon", preco=49.90, quantidade_estoque=10)
    p2 = Produtos(id_produto=2, nome="Caneca Dev", preco=25.00, quantidade_estoque=20)

    sistema.adicionar_produto(p1)
    sistema.adicionar_produto(p2)

    #Listando produtos
    sistema.lista_produtos()

    #Realizado vendas
    sistema.realizar_venda(id_produto=1, quantidade=3)
    sistema.realizar_venda(id_produto=2, quantidade=5)

    #Tentando vender mais do que o estoque
    sistema.realizar_venda(id_produto=1, quantidade=10)

    #Listando produtos novamente para ver o estoque atualizado
    sistema.lista_produtos()

# Simulação do banco de dados/estoque usando um dicionário
estoque = {
    "Produto A": 100,
    "Produto B": 50,
    "Produto C": 200
}

def adicionar_produto(nome_produto, quantidade):
    """Adiciona uma quantidade especificada ao estoque de um produto."""
    if nome_produto in estoque:
        estoque[nome_produto] += quantidade
        print(f"Adicionado{quantidade} unidades de '{nome_produto}'. Novo estoque: {estoque[nome_produto]}")
    else:
        #Se o produto não existe, ele é adicionado pela primeira vez
        estoque[nome_produto] = quantidade
        print(f" '{nome_produto}' adicionado ao estoque com {quantidade} unidades.")

def coletar_produto(nome_produto, quantidade):
    """Remove (coleta) uma quantidade especificada do estoque de um produto."""
    if nome_produto in estoque:
        if estoque[nome_produto] >= quantidade:
            estoque[nome_produto] -= quantidade
            print(f"Coletado {quantidade} unidsdea de '{nome_produto}'. Estoque restante: {estoque[nome_produto]}")
        else:
            print(f"Erro: Quantidade insuficiente de '{nome_produto}' em estoque.")
    else:
        print(f"Erro: '{nome_produto}' não encontrado no estoque.")

def visualizar_estoque():
    """Exibe todos os produtos e suas quantidades atuais no estoque."""
    print("\n--- Estoque Atual ---")
    for produto, quantidade in estoque.items():
        print(f" '{produto}' : {quantidade} unidades")
    print("-----------------------\n")

# Exemplo de uso das funções:
visualizar_estoque()

adicionar_produto("Produto A", 20)
adicionar_produto("Produto D", 50) # Adicionando um novo produto

visualizar_estoque()

coletar_produto("Produto B", 30)
coletar_produto("Produto A", 200) # Tentativa de coletar mais do que o disponível
coletar_produto("Produto E", 10) # Tentativa de coletar produto inexistente

visualizar_estoque()

import sqlite3

# 1. Função para conectar ao banco de dados e criar a tabela se não existir
def conectar_banco():
    conn = sqlite3.connect('produtos.db') # Conecta ou cria o arquivo do BD
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMEN,
            nome TEXT NOT NULL,
            preco REAL NOT NULL,
            codigo_barras TEXT UNIQUE
        )
    ''')
    # Confirma a criação da tabela
    conn.commit()
    print("Conexão estabelecida e tabela 'produtos' verificada/criada com sucesso.")

    # Retorna a conexão e o cursor para uso posterior
    return conn, cursor

except sqlite3.Error as e :
    print(f"Ocorreu um erro no SQLite: {e}")
    # Em caso de erro, é uma boa prática fechar a conexão
    if conn:
        conn.close()
    return None, None

#Exemplo de uso:
if __name__ == '__main__':
    conn, cursor = conectar_banco()
    if conn and cursor:
        # Aqui você pode adicionar maisoperações, como inserir dadoa, consultar, etc.
        # Por exemplo, para fechar a conexão no final:
        conn.close()