import pprint
import time

class vertice():

    def __init__(self, nombre):
        self.nombre = nombre
        self.color = ""

    def getNombre(self):
        return self.nombre

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def __repr__(self):
        return self.nombre+" ("+self.getColor()+")"

    def __equals__(self, other):
        return self.nombre == other.nombre

    def __cmp__(self, other):
        if self.nombre > other.nombre:
            res = -1
        elif self.nombre < other.nombre:
            res = 1
        else:
            res = 0
        return res

    def __hash__(self):
        return hash(self.nombre) ^ hash(self.color)

class arista():
    v1 = vertice
    v2 = vertice
    peso = int
    def __init__(self, v1, v2, peso):
        self.v1 = v1
        self.v2 = v2
        self.peso = peso

    def getV1(self):
        return self.v1

    def getV2(self):
        return self.v2
    
    def getPeso(self):
        return self.peso

    def getVNoColor(self):
        if self.getV1().getColor() == "":
            res = self.getV1()
        else:
            res = self.getV2()
        return res

    def getVColor(self):
        if self.getV1().getColor() != "":
            res = self.getV1()
        else:
            res = self.getV2()
        return res

    def sinColor(self):
        res = False
        if (self.getV1().getColor() == "" and
            self.getV2().getColor() == ""):
            res = True
        return res

    def conColor(self):
        res = False
        if ((self.getV1().getColor() != "") and
        (self.getV2().getColor() != "")):
            res = True
        return res
        
    def __repr__(self):
        return "("+self.v1.__repr__()+", "+self.v2.__repr__()+")"+" Peso: "+str(self.peso)

    def __equals__(self, other):
        return (self.v1, self.v2, self.peso) == (other.v1, other.v2, other.peso)

    def __cmp__(self, other):
        if self.peso > other.peso:
            res = 1
        elif self.peso < other.peso:
            res = -1
        else:
            res = 0
        return res

    def __hash__(self):
        return hash(self.v1) ^ hash(self.v2) ^ hash(self.peso)

class grafo():
    aristas = []
    def __init__(self, aristas):
        self.aristas = aristas

    def getAristas(self):
        return self.aristas

    def getVertices(self):
        res = []
        for i in self.aristas:
            res.append(i.getV1())
            res.append(i.getV2())
        return sorted(set(res), reverse = True)
                    
def coloracionRobusta(grafo, colores):
    res = []
    listaAristasAux = []
    vertices = grafo.getVertices()[:]
    aristas = grafo.getAristas()[:]
    pesoOptimo = 0
    n = len(vertices)
    aristaPesada = sorted(aristas, reverse = True)[0]
    mayorPeso = aristaPesada.getPeso()
    aristaPesada.getV1().setColor(colores[0])
    aristaPesada.getV2().setColor(colores[1])
    n = n - 2
    aristas.remove(aristaPesada)
    while n > 0:
        ac = mayorPeso
        for a in aristas:
            if ((a.getV1() == (aristaPesada.getV1())) or
            (a.getV2() == (aristaPesada.getV1())) or
            (a.getV1() == (aristaPesada.getV2())) or
            (a.getV2() == (aristaPesada.getV2()))):
                if (a.conColor() == False and a not in listaAristasAux):
                    listaAristasAux.append(a)
        aristaPesada = sorted(listaAristasAux, reverse = True)[0]
        for c in colores:
            pesoColor = 0
            ver = aristaPesada.getVNoColor()
            for ar in aristas:
                if ar.sinColor() == False:
                    if (ar.getV1().__equals__(ver) or
                        ar.getV2().__equals__(ver)):
                        if ar.getVColor().getColor() == c:
                            pesoColor = pesoColor + ar.getPeso()
            if pesoColor < ac:
                ac = pesoColor
                color = c
        pesoOptimo = pesoOptimo + ac
        ver.setColor(color)
        n = n - 1
        for aris in aristas:
            if aris.conColor() == True:
                if aris in listaAristasAux:
                    listaAristasAux = [rep for rep in listaAristasAux if rep != aris]
        aristas.remove(aristaPesada)
    res.append(vertices)
    res.append(pesoOptimo)
    return res
        
    






