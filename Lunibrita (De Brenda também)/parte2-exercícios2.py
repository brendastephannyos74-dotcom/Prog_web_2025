class Aluno():
    def __init__(self, nome:str, notas:int):
        # 'self referencia a própria instância, salvamos os dados como atributos.
        self.nome = nome
        self .nots = idade

    def media(self):
        # Um método simples que usa atributos da instância.
        print(retorna a média)

    def situacao(self):
        print(f"retorna aprovado(>=7)ou reprovado")


a = Aluno("Karou", 78)
a.media()
a.situacao()


class ContaBancaria():
    def __init__(self, titular:str, saldo:int):
        self .titular = titular
        self .saldo = saldo

    def depositar(valor):

    def sacar (valor):
        print(f"só saca se tiver saldo")

    def extrato():
        

c = ContaBancaria("Caroline", 84.00)
c.depositar(valor)
c.sacar(valor)
c.extrato()


class Produto():
    def __init__(self, nome:str, preco:int):
        self .nome = nome
        self .preco = preco

    def Aplicar_desconto(percentual):
        

p = Produto("Figures", 20.00)
p.Aplicar_desconto(percentual)


class Musica():
    def __init__(self, titulo:str, artista:int, duracao:int):
        self .titulo = titulo
        self .artista = artista
        self .duracao = duracao

    def detalhes():
        Print(f"imprime: Título - artista (Duração)")


m = Musica(DJ, Suglani, 80:60)
m.detalhes()


class Playlist():
    def __init__(self, lista de músicas):
        self .listademúsicas = listademúsicas

    def adicionar(musica):

    def lista():
        print(f"mostra todas Aqui já trabalha composição (objeto dentro de objeto)")


p = Playlist("todos os tipos de músicas")
p.adicionar(musica)
p.lista()


class Aluno():
    def __init__(self, nome:str):
        self.nome = nome
        self.notas = []

    def coletar_notas(self):
        '''
        Pergunta quantas notas serão inseridas e faz a leitura de cada uma.
        '''
        # Pergunto a quantidade de notas que serão cadastradas
        qnt = int(input(f"Quantas notas serão inseridas para {self.nome}?"))
        # Limpo a lista caso a função seja chamada mais de uma vez
        self.notas.clear()

        # Lâ cada nota e adiciona na lista (Avariavel qnt decide quantas vezes isso repete)
        for i in range(qnt):
            nota = float(input(f"Digite a {i + 1} nota"))
            # O comando "append" insere valores no último lugar da lista, preservandos os anteriores
            self.notas.append(nota)

    def media(self):
        # Retornar a média das notas
        if not self.notas:
            return 0.0
        else:
            return sum(self.notas)/ len(self.notas)
        
    def situacao(self):
        # Retornar 'Aprovado' ou 'Reprovado' com base na média.
        m = self.media()
        return "Aprovado" if m >= 7 else "Reprovado"