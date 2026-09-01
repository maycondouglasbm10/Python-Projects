from hash_table import HashTable
from user import User


def validar_cpf(cpf: str) -> bool:
    cpf = cpf.replace(".", "").replace("-", "").strip()
    return cpf.isdigit() and len(cpf) == 11


def menu():
    print("\n====== SISTEMA DE USUÁRIOS ======")
    print("1 - Cadastrar usuário")
    print("2 - Buscar usuário")
    print("3 - Remover usuário")
    print("4 - Verificar usuário")
    print("5 - Exibir tabela hash")
    print("6 - Sair")
    print("=================================")


def main():
    tabela = HashTable(capacity=10)

    while True:
        menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cpf = input("CPF: ").strip()

            if not validar_cpf(cpf):
                print("CPF inválido.")
                continue

            nome = input("Nome: ").strip()
            email = input("E-mail: ").strip()

            usuario = User(cpf, nome, email)

            tabela.insert(cpf, usuario)

            print("✓ Usuário cadastrado com sucesso!")

        elif opcao == "2":
            cpf = input("Digite o CPF: ").strip()

            usuario = tabela.get(cpf)

            if usuario:
                print("\nUsuário encontrado:")
                print(usuario)
            else:
                print("✗ Usuário não encontrado.")

        elif opcao == "3":
            cpf = input("Digite o CPF: ").strip()

            if tabela.delete(cpf):
                print("✓ Usuário removido.")
            else:
                print("✗ Usuário não encontrado.")

        elif opcao == "4":
            cpf = input("Digite o CPF: ").strip()

            if tabela.contains(cpf):
                print("✓ Usuário cadastrado.")
            else:
                print("✗ Usuário não cadastrado.")

        elif opcao == "5":
            tabela.display()

        elif opcao == "6":
            print("Programa encerrado.")
            break

        else:
            print("✗ Opção inválida.")


if __name__ == "__main__":
    main()