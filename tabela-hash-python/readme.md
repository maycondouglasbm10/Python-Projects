# 🗂️ Hash Table Users — Tabela Hash em Python

Uma implementação de **Tabela Hash em Python** para gerenciamento de usuários, desenvolvida com foco no estudo de **estruturas de dados, tratamento de colisões, fator de carga, redimensionamento automático e testes automatizados**.

O projeto foi desenvolvido como parte da minha jornada de aprendizado em **Python e desenvolvimento de software**, buscando aplicar conceitos de estruturas de dados em um projeto prático.

---

## 🎯 Objetivo

O objetivo deste projeto é implementar uma Tabela Hash do zero, sem utilizar estruturas prontas como `dict` para o armazenamento principal dos dados.

A aplicação permite cadastrar, buscar, verificar e remover usuários utilizando o **CPF como chave**.

Além disso, a implementação possui:

* Função hash própria
* Tratamento de colisões
* Separate Chaining
* Fator de carga
* Redimensionamento automático
* Rehashing dos elementos
* Testes automatizados com Pytest

---

## ✨ Funcionalidades

* 👤 Cadastro de usuários
* 🔎 Busca de usuários pelo CPF
* 🗑️ Remoção de usuários
* ✅ Verificação da existência de um usuário
* 📊 Visualização da estrutura da tabela
* 💥 Tratamento de colisões
* 📈 Redimensionamento automático da tabela
* 🔄 Rehashing dos elementos após o resize
* 🧪 Testes automatizados

---

## 🧠 Conceitos estudados

Durante o desenvolvimento foram aplicados conceitos importantes de estruturas de dados:

### Hash Function

A chave é transformada em um índice utilizando uma função hash.

```text
CPF → Função Hash → Índice → Bucket
```

### Colisões

Uma colisão acontece quando duas chaves diferentes produzem o mesmo índice.

Exemplo:

```text
1 → índice 1
5 → índice 1
```

Quando isso acontece, o projeto utiliza **Separate Chaining**, armazenando múltiplos elementos no mesmo bucket.

### Separate Chaining

Cada posição da tabela possui uma lista capaz de armazenar múltiplos elementos.

```text
[0] → vazio
[1] → 1 → João
       5 → Maria
[2] → 2 → Pedro
[3] → vazio
```

### Load Factor

O fator de carga representa a relação entre a quantidade de elementos e a capacidade da tabela:

```text
Load Factor = quantidade de elementos / capacidade
```

O projeto utiliza `0.75` como limite.

Quando o fator de carga ultrapassa esse valor, a tabela é redimensionada.

### Resize

A capacidade da tabela é dobrada:

```text
4 → 8
8 → 16
16 → 32
```

### Rehashing

Quando a capacidade muda, os índices calculados pela função hash também podem mudar.

Por isso, os elementos existentes precisam ser inseridos novamente na nova tabela.

```text
Tabela antiga
     ↓
Aumenta capacidade
     ↓
Cria novos buckets
     ↓
Calcula os hashes novamente
     ↓
Redistribui os elementos
```

---

## 🏗️ Estrutura do projeto

```text
tabela-hash-python/
│
├── src/
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

### `hash_table.py`

Contém a implementação da Tabela Hash, incluindo:

* Inserção
* Busca
* Remoção
* Verificação
* Função hash
* Fator de carga
* Resize
* Rehashing

### `user.py`

Define a estrutura do usuário utilizando `dataclass`.

Cada usuário possui:

```text
CPF
Nome
E-mail
```

### `main.py`

Contém a interface de linha de comando (CLI) utilizada para interagir com o sistema.

### `test_hash_table.py`

Contém os testes automatizados responsáveis por verificar o comportamento da Tabela Hash.

---

## 🖥️ Exemplo de utilização

Ao executar o programa, o usuário encontra um menu:

```text
====== SISTEMA DE USUÁRIOS ======

1 - Cadastrar usuário
2 - Buscar usuário
3 - Remover usuário
4 - Verificar usuário
5 - Exibir tabela hash
6 - Sair

=================================
```

Um usuário pode ser cadastrado utilizando seu CPF:

```text
CPF: 12345678901
Nome: João
E-mail: joao@email.com

✓ Usuário cadastrado com sucesso!
```

---

## 🧪 Testes automatizados

O projeto utiliza **Pytest** para validar o funcionamento da estrutura.

Atualmente existem **8 testes automatizados**, cobrindo:

* Inserção
* Busca
* Atualização
* Remoção
* Remoção de elemento inexistente
* Colisões
* Resize
* Preservação dos elementos após o resize
* Colisão + Resize + Rehashing

Resultado atual:

```text
8 passed
```

Para executar os testes:

```bash
python -m pytest
```

---

## 📊 Complexidade

| Operação         | Caso médio | Pior caso |
| ---------------- | ---------: | --------: |
| Inserção         |       O(1) |      O(n) |
| Busca            |       O(1) |      O(n) |
| Remoção          |       O(1) |      O(n) |
| Resize/Rehashing |       O(n) |      O(n) |

O desempenho médio é **O(1)** quando a função hash distribui os elementos de maneira adequada.

Em situações de muitas colisões, várias chaves podem acabar no mesmo bucket, aumentando o custo das operações.

---

## 🚀 Possíveis melhorias

Algumas melhorias que podem ser implementadas futuramente:

* [ ] Persistência dos usuários em banco de dados
* [ ] Validação completa de CPF
* [ ] Validação de e-mail
* [ ] Interface gráfica
* [ ] API REST
* [ ] Autenticação de usuários
* [ ] Logs da aplicação
* [ ] Testes de desempenho
* [ ] Integração contínua com GitHub Actions
* [ ] Dockerização do projeto

---

## 🛠️ Tecnologias utilizadas

* **Python**
* **Pytest**
* **Git**
* **GitHub**

---

## 📚 O que este projeto demonstra

Este projeto demonstra conhecimentos práticos em:

* Estruturas de dados
* Programação orientada a objetos
* Python
* Algoritmos
* Tratamento de colisões
* Gerenciamento de memória da estrutura
* Testes automatizados
* Organização de projetos
* Git e GitHub

---

## 👨‍💻 Autor

**Maycon Douglas**

Projeto desenvolvido como parte da minha jornada de aprendizado e construção de portfólio na área de **Tecnologia da Informação**.

---

⭐ Se este projeto foi útil para você, considere deixar uma estrela no repositório!
