import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from hash_table import HashTable


def test_insert_and_get():
    tabela = HashTable(5)

    tabela.insert("123", "João")

    assert tabela.get("123") == "João"


def test_update():
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