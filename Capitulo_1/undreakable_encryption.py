from secrets import token_bytes
from typing import Tuple

# gerando uma chave aleatória para usar como dados dummy de algo que queremos criptografar
# os dados dummy deverao ser combinados com os dados originais que queremos criptografar
# para isso, usaremos a operação lógica XOR, que retorna um booleano
def random_key(length: int) -> int:
    # gera length bytes aleatórios
    tb: bytes = token_bytes(length)
    # converte esses bytes em uma cadeia de bits e a devolve 
    return int.from_bytes(tb, 'big')


def encrypt(original: str) -> Tuple[int, int]:
    """
    Retorna uma chave criptografada aleatória gerada
    pelo dummy e original_key e o próprio dummy.
    """
    original_bytes: bytes = original.encode() # Transforma a Str Bytes b'223...
    dummy: int = random_key(len(original_bytes)) # Embaralha a Str "falsa"
    original_key: int = int.from_bytes(original_bytes, 'big') # Transforma os bytes em inteiros
    encrypted: int = original_key ^ dummy # roda o XOR aqui com o simbolo ^
    # encrypted é a chave "aleatória" criptografada, gerada pela junção do dummy e original_key
    print(f'chave encrypted={encrypted}')
    print(f'dummy={dummy}')
    return dummy, encrypted
    


def decrypt(key1: int, key2: int) -> str: # recebe as duas chaves (dummy e encryted)
    decrypted: int = key1 ^ key2 # XOR
    temp: bytes = decrypted.to_bytes((decrypted.bit_length()+7) // 8, 'big')
    return temp.decode()


if __name__ == "__main__":
    key1, key2 = encrypt('Pedro Moises Andrade dos Santos')
    result: str = decrypt(key1, key2)
    print(result)
