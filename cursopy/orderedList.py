#vetor ordenado
import numpy as np
class VetorOrdenado:
    def __init__(self, capacity):
        #atr capacidade recebe capacidade
        self.capacity = capacity
        #quando o vetor ta vazio, last position fica na ultima posição
        self.last_position = -1
        #values cria um vetor vazio com datatype = int 
        self.values = np.empty(self.capacity, dtype=int)
    
    def printV(self):
        #se a ultima posição for -1, a capacidade não foi alterada
        if self.last_position == -1:
            print('empty array')
        #imprime o vetor
        else:
            for i in range(self.last_position+1):
                print(i,' - ',self.values[i])
    
    def insert(self,value):
        #checa se a inserção não vai estourar a capacidade
        if self.last_position == self.capacity-1:
            print('max capacity reached')
            return
        pos = 0
        for i in range(self.last_position+1):
            pos = i
            if self.values[i] > value:
                break
            if i == self.last_position:
                pos = i+1
        x = self.last_position
        while x >= pos:
            self.values[x+1] = self.values[x]
            x -= 1
        self.values[pos] = value
        self.last_position += 1

vector = VetorOrdenado(10)
vector.printV()
vector.insert(8)
vector.insert(9)
vector.insert(1)
vector.insert(3)
vector.insert(2)
vector.insert(7)
vector.insert(5)
vector.printV()