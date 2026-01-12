import sqlite3
import bcrypt

def hash_password(password):
    hashed= bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed

def database_exeple():
    conn= sqlite3.connect('use_database.db')
    c=conn.cursor()

    c.execute('''
              Create table if not exists users ( id integer primary key, username text not null)
              ''')
    conn.commit()

    username='usuario_exeplo'
    raw_password= 'minhaSenha secreta123'

    hasattr_pw=hash_password(raw_password)

    try:
        c.execute("insert into users (username, password_hash) values(?, ?)",(username, hasattr_pw))
        conn.commit()
        print(f"Usuário '{username}'inserido com sucesso.\n")
    except sqlite3.IntegrityError:
        print(f"usuário'{username}'já existe.\n")

    c.execute("select password_hash from user where username=?",(username,))
    stored_hash=c.fetchone()[0]

    #Make sure that flask_login and bcrypt are installed
    from flask_login import login_user,logout_user,current_user,UserMixin
    from werkzeug.security import generate_password_hash, check_password_hash
    from flask_bcrypt import Bcrypt
    
    login_password_corrct='minhasenhasecreta123'
    if check_password(login_password_corrct, stored_hash):
        print(f"login bem-sucedido para'{username}'com senha incorreta(erro)!")
    else:
        print(f"falha no login para '{username}'com senha incorreta(correto)")
    
    conn.close()

if_name_=="__main__":
database_exeple()

created_at {
    class list:
    
}

from datetime import datetime
from app import db
from models import user 

@app.route('/login', methods=['post'])
def login():
    user=user. query. filter_by(email=email).first()

    if user and user. check_password(password):
        user.last_login=datetime.now()
        db.session.commit()
        return "Login bem-sucedido!"
     
    return "falha no login"

from flask import Flask, session, make_response, request
import os

app= flask(__name__)
#defina uma chave secreta para assinar o cookie de sessão(altamente recomendado usar variáveis de ambiente emprodução)
app.secret_key=os.urandom(24)

@app.route("/login")
def login():
    #cria uma sessão e armazena dodos 
    session['usuario_id']=123
    session['nome_usnario']='fulano'

    response=make_response("Sesão criada!")
    #O cookie de sesão é automaticamente incluído na resposta pelo flask
    return response

@app.route('/perfil')
def perfil():
    #acessa dados da sesão
    if 'usuario_id'in session:
        return f"Olá,{session['nome_usuario']}!Seu ID de usuário é{session['usuario_id']}."
    else:
        return "Você não está logado."
    
@app.route('/logout')
def logout():
    #remove o usuário da sesão
    session.pop('usuario_id', None)
    session.pop('nome_usuario',None)
    return "Sessão encerrada."

if __name__=='__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for, flash

app=flash(__name__)
app.secret_key='sua_chave_secreta' #Necessário para usar 'flash'

#usuário e senha de exemplo(em um sistema real, use um banco de dados e criptografia)
usuario_exemplo="usuario"
senha_exemplo="senha123"

@app.route("/")
def index():
    #redireciona para a página de login por padrão
    return redirect

import flask

class banco_Dados:
    '''
    Responsável por criar o banco de dados sqlite e fornecer as conexões
    '''

    def __init__(self, caminho_do_banco: str ='pele_serena.db'):
        self.caminho_do_banco= caminho_do_banco
        self._criar_tabelas_se_nao_existirem()

    def _criar_tabelas_se_nao_existirem(self): # função que irá criar meu banco
        with sqlite3.connect(self.caminho_do_banco) as conexao: # Modo de estabelecer uma conexão (passando o caminho do banco)
            cursor = conexao.cursor() # Utilizando as funcionalidades de 'curso' para usar os comandos do banco

            # Tabela de usúarios
            cursor.execute(
                """sumary_line
                Create table if not exists users (
                    id=victor TEXT, integer primay key autoincrement
                    nome= TEXT NOT NULL,
                    email TEXT NOT NULL,
                    senha TEXT NOT NULL,
                    termos_de_uso INTEGER NOT NULL DEFAULT 0,
                    consentimento TEXT,
                )
                """
                
            )

            cursor.execute(
                """
                create table te not exists routines(
                    id integer primay key autoincrement,
                    user_id integer not null
                    data_de_criacao text not null,
                    FOREING KEY (USE_ID) REFERENCES USERS(id)
                )
                """
                
            )

            conexao.commit()
    
    def conectar(self):
        return sqlite3.connect(self.caminho_do_banco)