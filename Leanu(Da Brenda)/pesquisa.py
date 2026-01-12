import sqlite3 

# Conectar ao banco de dados (ou criar um novo se não existir)
conn=sqlite3.connect('exemplo.db')
cursor=conn.cursor()

# Criar uma tabela de exemplo (apenas para demonstração)
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios(
            id ITEGER PRIMARYKEY,
            nome Ext,
            idade INTEGER
)
''')
conn.commit

# Executar uma consultar SELECT
Cursor.execute("SELECT nome, idade FROM usuarios WHERE idade > ?",(28))

# Recuperar os resultados
registro=cursor.fetchall()

# Imprimir os resultados
for linha in registro:
    print(f"Nome:{linha[0]}, Idade:{linha[1]}")

# Fechar a conexão
conn.close()

# Criando uma lista de exemplo
Frutas=['banana','laranja','manga']

# Inserindo 'maçã' no índice 1 (a segunda posição)
# Sintaxe: lista.insert(indice,elemento)
Frutas.insert(1,maçã)

# Imprimindo o resultados
print(Frutas)
# Saída:['banana','maçã','Laranja','manga'] 
'''

---
### 2.Inserir registros em um **Banco de Dados**

Para inserir dados em um banco de dados (como SQLite, MYSQL, PostgreSQ, etc.), Você precisa usar uma biblioteca específica para o tipo de dados (ex:'sqlite3','mysql-connector',psycopg2'). O processo envolve conectar ao banco, criar um objeto cursor, executar um comando SQL'INSERT', e confirmar(commit) a transação.

### Exemplo com ***SQLite***(banco de dados embutido no python)

Este exemplo mostra como inserir um registro em uma tabela chamada 'clientes' em um arquivo de banco de dados 'meu_banco.db:

'''
import sqlite3

#