# modelo do usuário

from dataclasses import dataclass


@dataclass # recurso do Python para facilitar a criação de classes que armazenam dados e cria automaticamente o __init__
class User:
    cpf: str
    nome: str
    email: str

    def __str__(self):
        return f"{self.nome} | CPF: {self.cpf} | E-mail: {self.email}"