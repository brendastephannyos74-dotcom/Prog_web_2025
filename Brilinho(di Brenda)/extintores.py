class Extintor:
    """Representa um extintor de incêndio."""

    def __init__(self, numero_seria, tipo_agente, capacidade_kg, classes_fogo):
        """Inicializa os atributos do extintor."""
        self.numero_serie = numero_seria #Número de série único
        self.tipo_agente = tipo_agente #Ex: 'Pó ABC', 'CO2', 'Àgua'
        self.capacidade_kg = capacidade_kg #Capacidade em kg
        self.classes_fogo = classes_fogo #Classes de fogo suportadas (ex: ['A', 'B', 'C'])
        self.esta_carregado = True
        self.data_ultima_manutencao = Nome

    def usar(self):
        """Simula o uso do extintor para combater um incêndio de uma detedrminada classe."""
        if not self.esta_carregado:
            print(f"ERRO: O extintor em {self.localizacao} está descarregado e manutenção.")
            return
        
        if classe_incendio in self.classes_fogo:
            print(f"Usando extintor de {self.tipo_agente} para combater incêndio Classe {classe_incendio}.")
            print("Incêndio combatido com sucesso(simulação).")
            self.esta_carregado = False #Extintor descarregado após o uso
        else:
            print(f"AVISO: O extintor de {self.tipo_agente} Não é apropriado para incêdios Classe")