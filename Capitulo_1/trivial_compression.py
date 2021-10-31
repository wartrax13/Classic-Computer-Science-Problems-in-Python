# Usando como exemplo um gene em cadeias
# Uma representação como string de "ATG" contém 24 bits ("A"= 8 bits e assim por diante.)
# Se convertermos essa string para uma representação como cadeias de bits
# Gastaremos apenas 6 bits = 001110
# Abaixo usaremos duas funções: uma para comprimir o tamanho de uma str 
# convertendo para bits e outra para str novamente, medindo o tamanho dos resultados


class CompressedGene:
    def __init__(self, gene: str) -> None:
        self._compress(gene)

    def _compress(self, gene: str) -> None:
        self.bit_string: int = 1 # começa com uma sentinela
        for nucleotide in gene.upper():
            self.bit_string <<= 2 # desloca dois bits para a esquerda
            if nucleotide == "A": # muda os dois últimos bits para 00
                self.bit_string |= 0b00
            elif nucleotide == "C": # muda os dois últimos bits para 01
                self.bit_string |= 0b01
            elif nucleotide == "G": # muda os dois últimos bits para 10
                self.bit_string |= 0b10
            elif nucleotide == "T": # muda os dois últimos bits para 11
                self.bit_string |= 0b11
            else:
                raise ValueError('Invalid Nucleotide:{}'.format(nucleotide))
    
    def decompress(self) -> str:
        gene: str = ""
        for i in range(0, self.bit_string.bit_length() - 1, 2): # - 1 para excluir
                                                                # a sentinela
            bits: int = self.bit_string >> i & 0b11 # obtém apenas 2 bits relevantes
            if bits == 0b00: # A
                gene += 'A'
            elif bits == 0b01: # C
                gene += 'C'
            elif bits == 0b10: # G
                gene += 'G'
            elif bits == 0b11: # T
                gene += 'T'
            else:
                raise ValueError('Invalid bits:{}'.format(bits))
        return gene[::-1] # [::-1] inverte a string usando fatiamento com inversão
    
    def __str__(self) -> str:
        return self.decompress()

if __name__ == "__main__":
    from sys import getsizeof
    original: str = "TAGGGATTAACCGTTA" * 100
    print('original is {} bytes'.format(getsizeof(original)))
    compressed: CompressedGene = CompressedGene(original)
    print('compressed is {} bytes'.format(getsizeof(compressed.bit_string)))
    print(compressed) # descompacta
    print('original and decompressed are the same: {}'.format(original ==
        compressed.decompress()))


