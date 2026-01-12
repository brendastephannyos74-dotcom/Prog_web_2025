from __future__ import annotations
import os, sqlite3, secrets, hashlib, hmac
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Optional, Tuple

from flask import Flask, render_template, request, redirect, make_response, g, url_for

#########################################################################
#                     Banco de Dados                                    #
#########################################################################

class Banco_Dados:

# primeiro passo: trabalhar com as importações

import os, sqlite3
from typing import Optional
from __future__ import annotations # Deixa o código mais boníto / legível
from flask import Flask, render_template, request, redirect, g, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash

#Começar a implementar as classes básicas

class BancoDeDados:
    #Sempre começo com meu costrutor - definindo o que a classe prcisa para funcionar

    def __init__(self, banco:str = "skinperfect.db"):
        self.banco = banco
        self.criar_tabela()

    def criar_tabela(self):
        conexao = sqlite3.connect(self.banco) 
        cursor = conexao.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXITS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT )
""")







        conexao.commit()
        conexao.close()
    
    def conectar(self):
        return sqlite3.connect(self.banco)
    
#Objeto de dominio usado para carregar dados do usuário
class UsuariaDados:
    def __init__(self, id:int, nome:str, email:str, last_login_at:Optional[str], termo_consentimento:bool, consentimento_at:Optional[str]):
        #Guardamos os canpos como atributos simples
        self.id = id
        self.nome = nome
        self.email = email
        self.last_legin_at = last_login_at
        self.termo_consentimento = termo_consentimento
        self.consentimento_at = consentimento_at

class RepositorioUsuarios:
    def __init__(self, db:BancoDeDados):
        self.db = db
         
    def criar_usuario(self, nome:str, email:str, senha:str, termo_consentimento: bool) -> UsuariaDados:
        email_normalizado = email.lower().strip()
        senha_hash = generate_password_hash(senha)
        consentimento_em = (datetime.utcnow().isoformat() if termo_consentimento else None)
        conexao = self.db.conectar()
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO users (nome, email, pwd_hash, termo_consentimento, consentimento_at) VALUES (?, ?, ?, ?, ?)"
                       (nome, email_normalizado, senha_hash, 1 if termo_consentimento else 0, consentimento_em),) ((email_normalizado,),)# "curso e id nome e esequilt ,"
        linha = cursor.fetchone()
        conexao.close()
        return linha
    
    def buscar_por_id(self, usuario_id: int):
        conexao = self.db.conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT id, nome, email, login_at, termo_consentimento_at FROM users WHERE id=?"
                       (usuario_id,),)
        r = cursor.fetchone()
        conexao.close()
        return