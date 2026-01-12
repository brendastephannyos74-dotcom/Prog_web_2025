#1. Classe de Entidade (Modelo de Domínio)
class Usuario:
    def __init__(self, id, nome, email):
        self.id = id
        self.nome = nome
        self.email = email

#2. Implementação do Repositório (utilizando uma lista em memória como exemplo)
class UsuarioRepository:
    def __init__(self):
        self._usuarios = [] # Simula um banco de dados

    def get_by_id(self, id):
        for u in self._usuarios:
            if u.id == id:
                return u
        return None
    
    def get_all(self):
        return list(self._usuarios)
    
    def add(self, usuario):
        self._usuarios.append(usuario)

    def update (self, usuario):
        #Lógica de atualização em memória
        for i, u in enumerate(self._usuarios):
            if u.id == usuario.id:
                self._usuarios[i] = usuario
                return
    
    def delete(self, id):
        self._usuarios =[u for u self._usuarios if u.id !=id]