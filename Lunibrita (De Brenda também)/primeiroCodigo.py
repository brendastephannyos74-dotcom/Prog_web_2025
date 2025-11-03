def saudacao (nome): # Para criar uma = Primeiro digitamos "def", depois o nome da função 
                       # e em seguida usamos () - que podem ter ou não variáveis.
                       # Outra nomeclatura para a váriavel aqui é chamado de "Parâmetro"
    print(f"Eael!, {nome}!") # "print" é o comando que imprime algo no terminal.

saudacao("Brenda") # Aqui está um exemplo sobre como ativar/chamar uma função = colocamos o nome dela
                  # e fornecemos o que ela precisa.

def soma(a, b):
    resultado = a + b
    return resultado

total = soma(6, 10)
print(total)

def subitracao(a, b):
    resultado = a - b
    return resultado

def multiplicacao(a, b):
    resultado = a * b
    return resultado

def divisao(a, b):
    print("Não realize divisão por 0")
    resultado = a / b
    return resultado
 
def media(a, b):
    resultado = (a + b) /2
    return resultado

print(subitracao(2, 1))
print(multiplicacao(5, 40))
print(divisao(10, 5))
print(media(8, 9))

centimetros =20 / 2
metros =44 / 2
print(f"{centimetros}cm é iquil a {metros}m")

import math

def calcular_area_cicunferecia(raio):
    #Calcula a área: A = h * r area =