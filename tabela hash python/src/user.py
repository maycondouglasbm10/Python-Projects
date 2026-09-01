from dataclasses import dataclass


@dataclass
class User:
    cpf: str
    nome: str
    email: str

    def __str__(self):
        return f"{self.nome} | CPF: {self.cpf} | E-mail: {self.email}"