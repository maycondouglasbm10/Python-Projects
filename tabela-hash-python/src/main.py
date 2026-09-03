#programa / menu

from hash_table import HashTable
from user import User


def validar_cpf(cpf: str) -> bool: # essa função é responsável por validar se o CPF fornecido é válido. Ela remove pontos e traços do CPF, verifica se ele contém apenas dígitos e se possui exatamente 11 caracteres. Retorna True se o CPF for válido e False caso contrário.
    cpf = cpf.replace(".", "").replace("-", "").strip()
    return cpf.isdigit() and len(cpf) == 11 # A função retorna True se o CPF contiver apenas dígitos e tiver exatamente 11 caracteres, indicando que é um CPF válido. Caso contrário, retorna False, indicando que o CPF é inválido.


def menu(): 
    print("\n====== SISTEMA DE USUÁRIOS ======")
    print("1 - Cadastrar usuário")
    print("2 - Buscar usuário")
    print("3 - Remover usuário")
    print("4 - Verificar usuário")
    print("5 - Exibir tabela hash")
    print("6 - Sair")
    print("=================================")


def main():# essa função é responsável por executar o programa principal, que consiste em um loop que exibe um menu de opções para o usuário interagir com a tabela hash. O usuário pode cadastrar, buscar, remover e verificar usuários, além de exibir a estrutura interna da tabela hash. A função continua executando até que o usuário escolha a opção de sair.
    tabela = HashTable(capacity=10)

    while True: #mantém o programa em execução até que o usuário escolha a opção de sair. O loop permite que o usuário interaja com a tabela hash repetidamente, realizando operações como cadastrar, buscar, remover e verificar usuários, além de exibir a estrutura interna da tabela hash.
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


if __name__ == "__main__": # essa condição verifica se o script está sendo executado diretamente (ou seja, não está sendo importado como um módulo em outro script). Se for o caso, a função main() é chamada para iniciar o programa. Isso permite que o código seja reutilizado como um módulo sem executar automaticamente a função main() quando importado.
    main()