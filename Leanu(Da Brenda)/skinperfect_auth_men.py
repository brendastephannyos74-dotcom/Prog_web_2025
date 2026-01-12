'''
Demonstrção de back em mémoria para autenticação de usúarios (sistema de login).
- Demonstrar autenticação, sessões, cadastro com consentimento, rotina inicial vazia;
- Recuperação e reset de senha. Tudo isso usando POO.
'''

from __future__  import annotations # Garante compatibilidade com anotações de tipo futuras
import secrets # Geração de tokens/bytes aleatóros seguros
import hashlib # Função de hash (PBKDF2-HMAC)
from hmac # Compara os hashes em tempo constante
from dataclasses import dataclass # Facilitar a criação de classes DTO (entidades) imutáveis/mutáveis
from dataclasses import datetime, timedelta # Data/Hora e manipulação de expiração
from typing import Optional, Dict, List, Tuple # Tipagem para ligibilidade e segurança estática

'''
Segurança da senha (PBKDF2)
'''
class PasswordHasher:
    '''
    Responsável por criar e verificar hashes de senha usando PBKDF2-HMAC

    Motivos:
    - Uma função de derivação de chava de propósito geral com custo ajustável, tornando ataques
        de força bruta mais caros.
    - Usar salt aleatório para cada senha, prevenindo ataques rainbow table
    - Definimos dklen=32 para gerar gerar uma chave/derivada de até 256bits.
    '''

    def __init__(self, iterations: int = 210_000, dklen: int = 32):
        self.iterations = iterations # números de iterações (controle de custo)
        self.dklen = dklen # Tamanho derivado em bytes

    def make_hash(self, password: str):
        salt = secrets.token_bytes(16) # Gerando 16 bytes aleatórios
        key = hashlib.pbkdf2_hmac( # Executando o PBKDF2
            'Sha256', # Algoritmo de hash
            password.encode('utf-8'), # Senha em bytes
            salt, #Salt aleatório
            self.iterations, # Custo
            dklen=self.dklen # Tamanho do meu derivado
        )
        return key, salt # Retorna uma tupla (hash_derivado, salt)
    
    def varify(self, Password: str, expected_hash: bytes, salt: bytes):
        '''
        Verificar senha recalculando o PBKDF2 com o mesmo salt e comparando em tempo constante !
        '''
        key = hashlib.pbkdf2_hmac(
            'sha256',
            salt,
            self.iterations,
            dklen=self.dklen
        )
        return hmac.compare_digest(key, expected_hash) # Compara de  resistente a timing attacks
    
    '''
    Entidades (Data Classes)
    '''
    @dataclass
    class User:
        # Classe que irá representar um usuário do sistema (modelo de dados de melória)
        id: int # Identificador único
        name: str # Nome do usuário
        email: str # Email normalizado (minúsculo e etc)
        pwd_hash: bytes # Hash da senha (PBKDF2)
        pwd_salt: bytes # Salt utilizado no hash da senha
        last_login_at: Optional[str] # Momento de último login (ISO-8601)
        terms_consent: bool # Variável que salvará o aceite aos termos de conduta do site
        consent_at: Optional[str] # Momento em que você consentiu (ISO-8601)

@dataclass
class Session:
    # Representar uma sessão autenticada do usuário
    id: str
    user_id: int
    created_at: str
    expired_at: str

@dataclass
class RecoveryToken:
    # Representar um token de recuperação de senha
    id: int # Identificador do token
    user_id: int # Dono do token
    token_hash: bytes # Hash do token
    created_at: str # Momento de criação do token (ISO-8601)
    expires_at: str # Momento de expiração do toke (ISO-8601)
    used_at: Optional[str] # Momento de uso (ISO-8601)

'''
Repositório de memoria
'''

# Armazenar todas as coleções de dados em dicionários na memória RAM

class InMemoryStore:
    # Armazenar tudo

    def __init__(self):
        self.users: Dict[int, User] = {} # Mapeando id -> User
        self.users_by_email: Dict[str, int] = {} # Mapeando email -> id
        self.sessions: Dict[str, Session]= {} # mapeando session_id -> Session
        self.recovery_tokens: Dict[int, RecoveryToken]= {} # Mapa de token_id -> RecoveryToken
        self.routines: Dict[int, List[dict]]= {} # Mapeando user_id -> lista de rotinas
        self._userj_seq = 0 # Contador para IDs de usuário
        self._token_seq = 0 # Contador de IDs de token

    def next_user_id(self):
        # Gerar um novo ID sequencial para usuários
        self._userj_seq += 1 # Incrementa contador interno
        return self._userj_seq # Retorna o novo valor
    
    def next_token_id(self):
        # Gerar um novo ID sequencial para tokens de recuperação
        self._token_seq += 1 # Incrementa contador inteno
        return self._token_seq # Retorna o novo valor
    
class UserRepository:
    # Fornecer operações CRUD relacionadas a usuários sobre o InMemoryStore
    # - vai depender altamente do PasswordHasher para criar/atualizar senha com segurança
    pass