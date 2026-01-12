class Pessoa():
    def __init__(self, nome:str, idade:int):
        # 'self referencia a própria instância, salvamos os dados como atributos.
        self.nome = nome
        self .idade = idade

    def apresentar (self):
        # Um método simples que usa atributos da instância.
        print(f"Olá, meu nome é {self.nome} e tenho{self.idade} anos.")


p = Pessoa("Manel", 30)
p.apresentar()


class Livro():
    def __init__(self, titulo:str, autor:int, preco:int):
        self .titulo = titulo
        self .autor = autor
        self .preco = preco

    def info (self):
        print(f"imprime essas informações formatadas")


L = Livro("Os nevi ciculos do poder", Livaxi, 40,00)
L.info()


class Carro():
    def __init__(self, modelo:str, cor:str):
        self .modelo : modelo
        self .cor : cor

    def dirigir(self):
        print(f"imprime algo como {"O carro X está em movimento"}")


C = Carro(Picape, cinsa)
C.dirigir()