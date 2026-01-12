class Calculadora:
    """
    Uma classe de calculadora simples que realiza operações aritméticas básicas.
    """
    def __init__(self, a, b):
         """
         Inicializa a calculadora com dois valores.
         """
         self.a = a
         self.b = b

    def soma(self):
         """
         Retorna a soma dos dois valores.
         """
         return self.a + self.b
    
    def subtrai(self):
         """
         Retorna a diferença entre os dois valores.
         """
         return self.a - self.b
    
    def multiplica(self):
         """
         Retorna o produto dos dois valores.
         """
         return self.a * self.b
    
    def divide(self):
         """
         Retorna o quociente da divisão dos dois valores.
         Lida com a divisão por zero.
         """
         if self.b == 0:
              return "Erro: Divisão por zero não é permitida."
         return self.a / self.b
    
#---Exemplo de usa---

#1. Solicita entrada do usuário
num1= float(input("Digite o primeiro número: "))
num2= float(input("Digite o segundo número: "))

#2. Cria um objeto de classe calculadora
calc= Calculadora(num1, num2)

#3. Chama os métodos e exibe os resultados
print(f"Soma: {calc.soma()}")
print(f"Subtração: {calc.subtrai()}")
print(f"Multiplicação: {calc.multiplica()}")
print(f"Divisão: {calc.divide()}")

class Caluladora:
    """
    Uma classe que representa uma calculadora com operações matemáticas básicas.
    """
    def adicionar(self, x, y):
         """Soma dois números."""
         return x + y
    
    def subtrair(self, x, y):
         return x - y
    
    def multiplicar(self, x, y,):
         """Multiplica dois números."""
         return x * y
    
    def dividir(self, x, y):
         """
         Divide o primeiro número pelo segundo.
         Retorna uma mensagem de erro se o divisor for zero.
         """
         if y == 0:
              return "Erro: Não é possível dividir por zero."
         return x / y
    
#---Exemplo de uso---

#1. Criar uma instância (obeto) da class calculadora
minha_calc = Calculadora()

#2. Realizar operções e imprimir os resutados
num1 = 10
num2 = 5

print(f"{num1} + {num2} = {minha_calc.adicionar(num1, num2)}")
print(f"{num1} - {num2} = {minha_calc.subtrair(num1, num2)}")
print(f"{num1} * {num2} = {minha_calc.multiplica(num1, num2 )}")
print(f"{num1} / {num2} = {minha_calc.dividir(num1, num2)}")

#3. Testar a divisão por zero
num3 = 45
num4 = 5
print(f"{num3} / {num4} = {minha_calc.dividir(num3, num4)}")
         
     
class CalculadoraSomaESubtracao:
     
    def __init__(self):
        pass
     
    def soma(self, a, b):
         resultado= a+b
         return resultado
    


class CalculadoraMultiplicacaoEDivisao:
     def __init__(self):
          pass
     
    def raiz_quadrada(self):
        pass



def soma(a, b):
     resultado = a + b
     return resultado

def subtracao(self, a, b):
     

import sqlite3

class BancoDeDados:
    def __init__(self, arquivo = 'banco.db'):
        self.arquivo = arquivo
        self.cria_tabela

    def conectar(self):
        conexao = sqlite3.connect(self.arquivo)
        return conexao
    
    def cria_tabela(self):
        conexao = self.conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            CRETE TABLE IF NOT EXISTS resultados(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                operacao TEXT,
                a INTEGER,
                b INTEGER,
                resultado REAL
            )
        """)

        conexao.commit()
        conexao.close()

    def salvar_valores(self, operacao, a, b, resultado):
        conexao = self.conectar()
        cursor = conexao.cursor()
        cursor.execute(
            "INSERT INTO resultados (operacao, a, b, resultado) VALUES (?, ?, ?, ?)"
            (operacao, a, b, resultado)
        ),
        conexao.commit()
        conexao.close()

    

class Calculadora:
    def __init__(self, banco):
        self.banco = banco

    def somar(self, a, b):
         resultado = a + b
         self.banco.salvar_valores("soma", a, b, resultado)
         return resultado
    
    def subtracao(self, a, b):
        resultado = a - b
        self.banco.salvar_valores("subtracao", a, b, resultado)
        return resultado
    
    def multiplicacao(self, a, b):
        resultado = a * b
        self.banco.salvar_valores("multiplicacao", a, b, resultado)
        return resultado
    
    def divusao(self, a, b):
        if b == 0:
            print("Erro: Divisão por zero não é permitida!")
            return Nome
        else:
         resultado = a / b
         self.banco.salvar_valores("divisao", a, b, resultado)
         return resultado
        
def main():
    banco = BancoDeDados()
    banco.cria_tabela()
    Calculadora= Calculadora(banco)

    while True:
     print("Bem-Vindo a nossa calculadora!")
     print("------------------------------------")
     print("[1] - Somar!")
     print("[2] - Subtrair!")
     print("[3] - Multiplica!")
     print("[4] - Dividir!")

     opcao = input("Escolha uma opção: ")

    if opcao == "0":
        print("Encerrando a nossa calculadora, tchau!")
        break
    elif opcao not in {"1", "2", "3", "4"}:
        print("Opção inválida. Tente novamente.")
        continue
    prímeiro = input("Digite o primeiro número intero: ")
    segundo = input("Digite o segundo número inteiro: ")

    if not (primeiro.isdigit() and segundo.isdigit):
        print("Erro: Digite apenas número inteiros positivos.")
        continue
    a = int (primeiro)
    b = int (segundo)

    if opcao == "1":
        resultado = Calculadora.somar(a, b)
        print("O resultado é: ", resultado)
    elif opcao == "2":
        resultado = Calculadora.subtracao(a, b)
        print("O resutado é: ", resultado)
    elif opcao == "3":
        resultado = Calculadora.multiplicacao(a, b)
        print("O resutado é: ", resultado)
    elif opcao == "4":
        resultado = Calculadora.divisao(a, b)
        print("O resultado é: ", resultado)

if __name__ == "__main__":
    main()