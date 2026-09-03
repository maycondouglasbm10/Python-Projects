#cérebro da tabela hash 

from typing import Optional


class HashTable:
    def __init__(self, capacity: int = 10):
        if capacity <= 0:
            raise ValueError("A capacidade deve ser maior que zero.")

        self.capacity = capacity
        self.size = 0 # representa quantos elementos existem atualmente na tabela.
        self.max_load_factor = 0.75 # "quando a tabela passar de 75% de ocupação, vamos redimensioná_la"
        self.buckets = [[] for _ in range(capacity)] #cria as "gavetas" da tabela hash, que são listas vazias onde os elementos serão armazenados.

    def _resize(self):
        old_capacity = self.capacity
        old_buckets = self.buckets


        self.capacity *= 2

        print(f"\n⚠️ Fator de carga excedido!")
        print(f"🔄 Redimensionando tabela: {old_capacity} → {self.capacity}")
        print("♻️ Recalculando índices dos elementos...")

        self.buckets = [[] for _ in range(self.capacity)]

        for bucket in old_buckets:
            for item in bucket:
                key, value = item
                index = self._hash(key)
                self.buckets[index].append([key,value])
        print("✅ Redimensionamento concluído!\n")

    def _hash(self, key: str) -> int:
        """
        Converte a chave (cpf) em um índice da tabela.
        """
        hash_value = 0

        for char in key:
            hash_value = (hash_value * 31 + ord(char)) % self.capacity

        return hash_value

    def insert(self, key: str, value) -> None: # colocar um elemento na tabela.
        """
        Insere ou atualiza um elemento.
        """
        index = self._hash(key)# calcula o índice da "gaveta" correspondente à chave fornecida usando a função de hash. Em seguida, obtém a "gaveta" (uma lista) na posição do índice calculado.
        bucket = self.buckets[index] 

        for item in bucket: # percorre a "gaveta" correspondente ao índice calculado para verificar se a chave já existe. Se existir, atualiza o valor associado a essa chave. Caso contrário, adiciona um novo par chave-valor à "gaveta".
            if item[0] == key:
                item[1] = value
                return

        bucket.append([key, value]) # se a chave não existir, adiciona um novo par chave-valor à "gaveta" correspondente ao índice calculado.
        self.size += 1

        if self.load_factor() > self.max_load_factor:
            self._resize()

    def get(self, key: str) -> Optional[object]: # essa função é responsável por buscar um elemento na tabela hash com base na chave fornecida. Ela retorna o valor associado à chave, se encontrado, ou None caso a chave não exista na tabela.
        """
        Busca um elemento pela chave.
        """
        index = self._hash(key)

        for item in self.buckets[index]:
            if item[0] == key:
                return item[1]

        return None

    def delete(self, key: str) -> bool: # essa função é responsável por remover um elemento da tabela hash com base na chave fornecida. Ela retorna True se a remoção for bem-sucedida (ou seja, se a chave existir e o elemento for removido) e False caso contrário (ou seja, se a chave não existir na tabela).
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

    def contains(self, key: str) -> bool: # essa função é responsável por verificar se uma determinada chave existe na tabela hash. Ela retorna True se a chave estiver presente na tabela e False caso contrário.
        return self.get(key) is not None

    def load_factor(self) -> float: # essa função calcula o fator de carga da tabela hash, que é uma medida da densidade da tabela. O fator de carga é calculado como a razão entre o número de elementos armazenados na tabela (self.size) e a capacidade total da tabela (self.capacity). Um fator de carga mais alto indica que a tabela está mais cheia, enquanto um fator de carga mais baixo indica que há mais espaço disponível para novos elementos.
        return self.size / self.capacity

    def display(self) -> None: # essa função exibe a estrutura interna da tabela hash, mostrando o conteúdo de cada "gaveta" (bucket) da tabela. Ela percorre todas as "gavetas" e imprime os pares chave-valor armazenados em cada uma delas, além de exibir informações sobre o número total de elementos, a capacidade da tabela e o fator de carga.
       
        print("\n========== TABELA HASH ==========")

        for index, bucket in enumerate(self.buckets): # percorre todas as "gavetas" da tabela hash, usando a função enumerate para obter tanto o índice da "gaveta" quanto o conteúdo da "gaveta" em si. Para cada "gaveta", ele imprime o índice e, em seguida, verifica se a "gaveta" está vazia ou contém elementos. Se estiver vazia, imprime "Vazio". Caso contrário, percorre os pares chave-valor na "gaveta" e os imprime no formato "chave -> valor", separados por "|".
            print(f"[{index}] ", end="")

            if not bucket: # verifica se a "gaveta" está vazia. Se estiver vazia, imprime "Vazio" e continua para a próxima "gaveta". Caso contrário, percorre os pares chave-valor na "gaveta" e os imprime no formato "chave -> valor", separados por "|".
                print("Vazio")
                continue

            for key, value in bucket: # percorre os pares chave-valor na "gaveta" e os imprime no formato "chave -> valor", separados por "|". O parâmetro end=" | " é usado para evitar a quebra de linha após cada par, permitindo que todos os pares sejam impressos na mesma linha. Após imprimir todos os pares da "gaveta", ele imprime uma nova linha para separar as "gavetas" na saída.
                print(f"{key} -> {value}", end=" | ")

            print()

        print("=================================")
        print(f"Elementos: {self.size}")
        print(f"Capacidade: {self.capacity}")
        print(f"Fator de carga: {self.load_factor():.2f}")