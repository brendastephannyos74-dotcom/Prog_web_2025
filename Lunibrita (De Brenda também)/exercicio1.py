def verificar_idade(idade):
    # Se a idade for 18 ou mais, é maior de idade
    if idade >= 18:
        return "Maior de idade"
    else:
        return "Menor de idade"

# Exemplos de uso
print(verificar_idade(17))
print(verificar_idade(25))