# -*- coding: utf-8 -*-
import punt
import math 
class Poligon():
    def __init__(self, vertexs = []):
        assert len(vertexs)==0 or len(vertexs)>2
        self._vertexs = vertexs
    
    def afegeixVertex(self, pt):
        self._vertexs.append(pt)
                
    def perimetre(self):
        perimetre = 0
        for index in range(len(self._vertexs) - 1):
            perimetre += (self._vertexs[index] - self._vertexs[index+1])
        perimetre += (self._vertexs[0] - self._vertexs[-1])
        return perimetre
    
    def area(self):
        raise NotImplementedError('implementat a les subclasses')
    
    def __str__(self):
        resultat = "["
        for v in self._vertexs:
            resultat = resultat + str(v)
        resultat = resultat + "]"
        return resultat

class Triangle(Poligon):
    def __init__(self,vertexs=list()):
        assert (len(vertexs)==3)
        super().__init__(vertexs)

    def afegeixVertex(self, pt):
        raise Exception("No es poden afegir vértexs a un triangle")
    
    def area(self):
        a=self._vertexs[0]-self._vertexs[1]
        b=self._vertexs[1]-self._vertexs[2]
        c=self._vertexs[0]-self._vertexs[2]
        s=(a+b+c)/2
        area=math.sqrt(s*(s-a)*(s-b)*(s-c))
        return(area)
class Quadrat(Poligon):
    def __init__(self,vertexs=list()):
        assert (len(vertexs)==4)
        super().__init__
        self._costat=self._vertexs[0]-self._vertexs[3]
        for i in range(len(self._vertexs)-1):
            assert (self._vertexs[i]-self._vertexs[i+1]==self._costat)
            
    @property
    def costat(self):
        return(self._costat)
   
    def afegeixVertex(self,pt):
        raise Exception("No es poden afegir vertexs a un quadrat")
        
    def area(self):
        return(self._costat**2)
        
    def perimetre(self):
        return(4*self._costat)
    
