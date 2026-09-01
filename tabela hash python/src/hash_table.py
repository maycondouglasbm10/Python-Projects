from typing import Optional


class HashTable:
    def __init__(self, capacity: int = 10):
        if capacity <= 0:
            raise ValueError("A capacidade deve ser maior que zero.")

        self.capacity = capacity
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]

    def _hash(self, key: str) -> int:
        """
        Converte a chave em um índice da tabela.
        """
        hash_value = 0

        for char in key:
            hash_value = (hash_value * 31 + ord(char)) % self.capacity

        return hash_value

    def insert(self, key: str, value) -> None:
        """
        Insere ou atualiza um elemento.
        """
        index = self._hash(key)
        bucket = self.buckets[index]

        for item in bucket:
            if item[0] == key:
                item[1] = value
                return

        bucket.append([key, value])
        self.size += 1

    def get(self, key: str) -> Optional[object]:
        """
        Busca um elemento pela chave.
        """
        index = self._hash(key)

        for item in self.buckets[index]:
            if item[0] == key:
                return item[1]

        return None

    def delete(self, key: str) -> bool:
        """
        Remove um elemento pela chave.
        """
        index = self._hash(key)
        bucket = self.buckets[index]

        for item in bucket:
            if item[0] == key:
                bucket.remove(item)
                self.size -= 1
                return True

        return False

    def contains(self, key: str) -> bool:
        return self.get(key) is not None

    def load_factor(self) -> float:
        return self.size / self.capacity

    def display(self) -> None:
        """
        Exibe a estrutura interna da tabela.
        """
        print("\n========== TABELA HASH ==========")

        for index, bucket in enumerate(self.buckets):
            print(f"[{index}] ", end="")

            if not bucket:
                print("Vazio")
                continue

            for key, value in bucket:
                print(f"{key} -> {value}", end=" | ")

            print()

        print("=================================")
        print(f"Elementos: {self.size}")
        print(f"Capacidade: {self.capacity}")
        print(f"Fator de carga: {self.load_factor():.2f}")