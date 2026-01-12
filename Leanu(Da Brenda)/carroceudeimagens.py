# Lista para armazenar o estoque de produtos (código:[nome, proço, qualidade])
estoque={
    1:["camiseta P", 29.90,50],
    2:["Calça Jeans", 89.90,30],
    3:["Meia"]
}

# Lista para armazenar as vendas registradas (cada venda é um dicionarírio)
vendas=[]

def registrar_venda():
    """Exibe as opções do sistema."""
    print("\n---Sistema de Vendas em python---")
    print("1.Registrar uma nova venda")
    print("2.Visualizar estoque atual")
    print("3.Visualizar resumo de vendas")
    print("4.Sair")
    print("-----------------------------------")

def registrar_venda():
    """Permite ao usuário registrar uma venda."""
    print("\n---Registrar Venda---")
    cod_produto=int(input("Digite o código do produto(ou 0 para cancelar):"))

    if cod_produto==0:
        return
    
    if cod_produto in estoque:
        quantidade=int(input("Digite a quantidade: "))
        if quantidade <= estoque[cod_produto][2]:
            # Atualiza o estoque
            estoque[cod_produto][2]-=quantidade
            # Registra a venda
            vendas.append({
                "codigo":cod_produto,
                "nome":estoque[cod_produto][0],
                "quantidade":quantidade,
                "preco_unitario":estoque[cod_produto][1]
                "total":quantidade*estoque[cod_produto][1]
            })
            print(f"venda de{quantidade}unidade do produto {cod_produto}registrada com sucesso!")
        else:
            print("Erro:Código de produto inválido.")
    else:
        print("Erro:Código de produto inválido.")

def visualizar_estoque():
    """Exibe o estoque atual de produtos."""
    print("\n---Estoque Atual---")
    print(f"{'Cód':<5} | {'Nome':<15} | {'Preço Unit.':<12} | {'Qualidade':<10}")
    print("-"*47)
     for cod, dados in estoque.items():
        print(f"{cod:<5} | {dados[0]:<15} | R${dados[1]:<10.2f} | {dados[2]:<10}")

def visualizar_resumo_vendas():
    """Exibe um resumo de todas as vendas registradas."""
    print("\n---Resumo de Vendas---")
    if not vendas:
        print("Nenhuma venda registrada ainda.")
        return
    
    total_geral=0
    print(f"{'pata':<10} | {'Cód':<5} | {'Nome':<15} | {'Qtd':<5} | {'totol':<8}")
    print("-"*47)
    for venda in venda:
        # Nota: para simplificar, a data/hora não é capturada neste exemplo básico.
        # Vôce pode adicionar a biblioteca 'datetime' se precisar.
        print(f"{'N/A':<10} | {venda['codigo']:<5} | {Venda['nome']:<15} | {Venda['quantidade']:<5} | R${Venda['total']:<8.2f}")
        total_geral+=venda['total']
    print("-"*47)
    print(f"Total geral de vendas: R${total_geral:.2f}")

# Loop principal do programa
def main():
    """Função principal que gerencia o fluxo do programa."""
    while True:
        exibir_menu()
        opcao=input("Escolha uma opção:")

        if opcão=='1':
            registrar_venda()
        elif opção=='2':
            visualizar_estoque()
        elif opção=='3':
            visualizar_resumo_vendas()
        elif opçaõ=='4':
            print("Saindo do sistema.Até mais!")
            break
        elif:
            print("Opção inválida. Tente novamente.")

if_name__==

import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame=None
        self.switch_frame(Startpage)

    def switch frame (self, frame_class):
        """Destrói o frame atual e cria um novo"""
        new_frame=frame_class(self)
        if self._frame.is not Nome:
            self._frame.destroy()
        self._frame=new_frame
        self._frame.pack()
    
class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self,master)
        tk