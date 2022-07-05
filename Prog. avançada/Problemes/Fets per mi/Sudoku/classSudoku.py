import numpy as np

class Sudoku:
    def __init__(self,nomFitxer=' '):
        self._plantilla=np.loadtxt(nomFitxer, int)
        self._sud=np.loadtxt(nomFitxer, int)
    def introduirNum(self,valor,fila,columna):
        fila -=1
        columna -=1
        f=(fila//3)*3
        c=(columna//3)*3
        assert self._plantilla[fila,columna]==0,"\nAquest número ja està la sudoku original"
        assert 0<valor<10, "\nAquest nombre es erroni"
        if self._sud[fila,columna]==0:
            assert valor not in self._sud[fila,:], "\nAquest nombre ja està la fila"
            assert valor not in self._sud[:,columna], "\nAquest nombre ja està a la columna"
            assert valor not in self._sud[f:f+3,c:c+3],"\nAquest nombre ja està en el cuadrant de 3*3"  
            self._sud[fila,columna]=valor
    def eliminar(self,fila,columna):
        fila -=1
        columna -=1
        if self._plantilla[fila,columna]==0:
            self._sud[fila,columna]=0
        else:
            print("\nAquest nombre està al sudoku original")
    def mostra(self):
        print(self._sud)
    def complete(self):
        if 0 not in self._sud:
            return(True)
        else:
            return(False)
    
    
    
