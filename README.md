# 🔐 Hash Table User Manager

Sistema de gerenciamento de usuários desenvolvido em Python utilizando uma **Tabela Hash implementada manualmente**, com tratamento de colisões através de encadeamento separado.

## 📌 Sobre o projeto

O objetivo deste projeto é demonstrar, na prática, o funcionamento de uma estrutura de dados do tipo **Hash Table**.

O sistema permite:

* Cadastrar usuários
* Buscar usuários pelo CPF
* Remover usuários
* Verificar se um usuário existe
* Visualizar a estrutura interna da tabela
* Observar o fator de carga da tabela
* Tratar colisões utilizando listas encadeadas

## 🧠 Conceitos utilizados

* Tabela Hash
* Função Hash
* Colisões
* Separate Chaining
* Estruturas de dados
* Complexidade de algoritmos
* Programação Orientada a Objetos
* Dataclasses
* Testes automatizados
* Interface de linha de comando (CLI)

## 📂 Estrutura

```text
hash-table-users/
│
├── src/
│   ├── __init__.py
│   ├── hash_table.py
│   ├── user.py
│   └── main.py
│
├── tests/
│   └── test_hash_table.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

## ⚙️ Como funciona

O CPF do usuário é utilizado como chave.

Exemplo:

```text
CPF: 12345678900
Nome: João Silva
```

A função hash transforma a chave em um índice:

```text
"12345678900"
       ↓
   função hash
       ↓
    índice 7
       ↓
   bucket[7]
       ↓
CPF → usuário
```

## 💥 Tratamento de colisões

Uma colisão acontece quando duas chaves diferentes produzem o mesmo índice.

Exemplo:

```text
CPF A ─────┐
           ├──→ índice 3
CPF B ─────┘
```

O projeto utiliza **Separate Chaining** para resolver esse problema:

```text
Bucket 3

[
    [CPF_A, Usuário A],
    [CPF_B, Usuário B]
]
```

Dessa maneira, diferentes elementos podem ocupar o mesmo índice.

## ⏱️ Complexidade

Em condições ideais:

| Operação | Complexidade média |
| -------- | -----------------: |
| Inserção |               O(1) |
| Busca    |               O(1) |
| Remoção  |               O(1) |

No pior caso, quando ocorrem muitas colisões:

| Operação | Pior caso |
| -------- | --------: |
| Inserção |      O(n) |
| Busca    |      O(n) |
| Remoção  |      O(n) |

## ▶️ Como executar

Clone o projeto:

```bash
git clone SEU_REPOSITORIO
```

Entre na pasta:

```bash
cd hash-table-users
```

Execute:

```bash
python src/main.py
```

## 🧪 Executando os testes

Instale o pytest:

```bash
pip install pytest
```

Execute:

```bash
pytest
```

## 🎯 Objetivo acadêmico/profissional

Este projeto foi desenvolvido para demonstrar conhecimentos em:

* Estruturas de dados
* Algoritmos
* Python
* Organização de projetos
* Testes automatizados
* Análise de complexidade
* Tratamento de colisões

## 🚀 Possíveis melhorias

Futuras versões podem incluir:

* Redimensionamento automático da tabela
* Persistência em banco de dados
* API REST
* Interface web
* Autenticação
* Hash seguro de senhas
* Logs de operações
* Docker
* CI/CD
* Testes de performance

## 📜 Licença

Este projeto está disponível para fins educacionais.
