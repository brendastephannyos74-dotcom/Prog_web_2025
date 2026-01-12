class Maquiagem:
    def __init__(self, tipo_produto, cor, marca):
        self.tipo_produto = tipo_produto
        self.cor = cor
        self.marca = marca
        self.aplicado = False

    def aplicar(self):
        if not self.aplicado:
            print(f"Aplicando{self.tipo_produto} na cor {self.cor} da marca {self.marca}.")
            self.aplicado= True
        else:
            print(f"Aplicando {self.tipo_produto}já está aplicado.")

#Exemplo de uso de classe:
batom = Maquiagem("Batom", "Vermelho Intenso", "Baco Rosa Beauty")
sonbra = Maquiagem("Sombra", "Cobre", "MAC")

batom.aplicar()
sombra.aplicar()
    
class HigienePessoa:
    """
    Representa uma pessoa e seus hábitos básicos de higiene.
    """
    def __init__(self, nome):
        self.nome = nome
        self.maos_limpas = False
        self.dentes_escovados = False
        self.babho_tomado = False

    def lavar_maos(self):
        """Ação de lavar as mãos."""
        self.maos_limpas = True
        print(f"{self.nome}lavou as mãos.")

    def escovar_dentes(self):
        """Ação de escovar os dentes."""
        self.dentes_escovados = True
        print(f"{self.nome}escovou os dentes.")

    def tomar_banho(self):
        """Ação de tomar banho."""
        self.banho_tomado = True
        print(f"{self.nome}tomou banho.")

    def verificar_higiene(self):
        """Verifica o estado geral de higiene."""
        if self.maos_limpas and self.dentes_escovados and self.bonho_tomado:
            return f"{self.nome}está com a higiene em dia."
        else:
            return f"{self.nome}precisa melhorar a higiene."

# Exemplo de uso:
pedro = Pessoa("Pedro")
pedro.lavar_maos()
pedro.escovar_dentes()
pedro.tomar_banho()
pedro(pedro.verificar_higiene())

class cabelo:
    """
    Representa as características e
    """
    