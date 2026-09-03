#testes 

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from hash_table import HashTable


def test_insert_and_get(): # essa função de teste verifica se a inserção e a recuperação de elementos na tabela hash estão funcionando corretamente. Ela cria uma instância da tabela hash, insere um par chave-valor e, em seguida, verifica se o valor pode ser recuperado corretamente usando a chave.
    tabela = HashTable(5)

    tabela.insert("123", "João")

    assert tabela.get("123") == "João"


def test_update(): # essa função de teste verifica se a atualização de um elemento na tabela hash está funcionando corretamente. Ela cria uma instância da tabela hash, insere um par chave-valor, atualiza o valor associado à mesma chave e, em seguida, verifica se o valor atualizado pode ser recuperado corretamente usando a chave.
    tabela = HashTable(5)

    tabela.insert("123", "João")
    tabela.insert("123", "Maria")

    assert tabela.get("123") == "Maria"


def test_delete():
    tabela = HashTable(5)

    tabela.insert("123", "João")

    assert tabela.delete("123") is True
    assert tabela.get("123") is None


def test_delete_nonexistent():
    tabela = HashTable(5)

    assert tabela.delete("999") is False


def test_collision():
    tabela = HashTable(1)

    tabela.insert("123", "João")
    tabela.insert("456", "Maria")

    assert tabela.get("123") == "João"
    assert tabela.get("456") == "Maria"

def test_resize():
    tabela = HashTable(4)

    tabela.insert("1", "João")
    tabela.insert("2", "Maria")
    tabela.insert("3", "Pedro")
    tabela.insert("4", "Ana")

    assert tabela.capacity == 8

def test_resize_keeps_elements():
    tabela = HashTable(4)

    tabela.insert("1", "João")
    tabela.insert("2", "Maria")
    tabela.insert("3", "Pedro")
    tabela.insert("4", "Ana")

    assert tabela.get("1") == "João"
    assert tabela.get("2") == "Maria"
    assert tabela.get("3") == "Pedro"
    assert tabela.get("4") == "Ana"

def test_collision_and_resize():
    tabela = HashTable(4)

    # "1" e "5" geram o mesmo indice na capacidade 4 
    tabela.insert("1", "João")
    tabela.insert("5", "Maria")

    #inserimos mais elementos para forçar o resize
    tabela.insert("2", "Pedro")
    tabela.insert("3", "Ana")

    #a capacidade deve ter dobrado 
    assert tabela.capacity == 8

    #todos os elemenetos devem continuar acessiveis
    assert tabela.get("1") == "João"
    assert tabela.get("5") == "Maria"
    assert tabela.get("2") == "Pedro"
    assert tabela.get("3") == "Ana"