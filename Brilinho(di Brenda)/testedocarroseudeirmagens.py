class cabalo:
    """
    Representa as caranta as características e métodos relacionados ao cabelo.
    """
    def __init__(self, cor, tipo_curvatura, comprimento):
        """
        Método construtor para inicializar os atributos do cabelo.
        """
        self.cor = cor
        #Tipos de curvatura: 1 (liso), 2abc (ondulado), 3abc (cacheado), 4abc (crespo)
        self.tipo_curvatura = tipo_curvatura
        self.esta_limpo = True
    
    def lavar(self):
        """
        Método para simular o corte do cabelo.
        """
        self.comprimento = novo_comprimento
        print(f"O cabelo foi cortado. Novo comprimento: {self.comprimento} cm.")

    def sujar(self):
        """
        Método para simular que o cabelo ficou sujo.
        """
        self.esta_limpo = False
        print(f"O cebelo{self.cor} está sujo agora.")

# Exemplo de uso (instanciando um objeto)
meu_cabelo = Cabelo(cor="castanho", tipo_curvatura="3B", comprimento=30)

print(f"Meu cabelo é {meu_cabelo.cor}, tipo {meu_cabelo.tipo_curvatura} e tem {meu_cabelo.comprimento} cm.")
meu_cabelo.lavar()
meu_cabelo.sujar()
meu_cabelo.lavar()
meu_cabelo.cortar()



#Dicionário para armazenar o estoque: {código_produto: [nome_produto, quantidade, preco]}
estoque = {
    1:["Camiseta P", 10, 29.90],
    2:["Calça Jeans", 5, 89.90],
    3:["Meia", 50, 9.90],
}

def listar_produtos():
    """Exibe todos os produtos e o estoque atual."""
    print("\n---ESTOQUE ATUAL ---")
    print(f"{'CÁDIGO':<10} {'PRODUTO':<20} {'QTD':<10} {'PREÇO R$':<10}")
    for codigo, dados in estoque.items():
        nome, quantidade, preco = dados
        print(f"{codigo:<10} {nome:<20} {quantidade:<10} {preco:<10.2f}")
    print("---------------------\n")

def realizar_venda():
    """Permite """