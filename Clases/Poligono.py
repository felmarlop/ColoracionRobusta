"""
Objeto: Poligono
Atributos: Lista de coordenadas
"""
from Clases.Recta import *
from Libs.graphics import *
from Util.CaminosDeLee import *

class poligono():
    coordenadas = []
    def __init__(self, coordenadas):
        self.coordenadas = coordenadas
    
    def getCoordenadas(self):
        return self.coordenadas
    
    def setCoordenadas(self, newCoordenadas):
        self.coordenadas = newCoordenadas
    
    def __repr__(self):
        return self.coordenadas.__repr__()
    
    def coordenadaMayorAbscisa(self):
        res = coordenada
        if(self.coordenadas == []):
            res = coordenada(0, 0)
        else:
            res = sorted(self.coordenadas, key = lambda 
                         coordenada: coordenada.x)[-1]
        return res
    
    def coordenadaMenorAbscisa(self):
        res = coordenada
        if(self.coordenadas == []):
            res = [0,0]
        else:
            res = sorted(self.coordenadas, key = lambda
                       coordenada: coordenada.x)[0]
        return res
    
    def coordenadaMayorOrdenada(self):
        res = coordenada
        if(self.coordenadas == []):
            res = coordenada(0,0)
        else:
            res = sorted(self.coordenadas, key = lambda
                       coordenada: coordenada.y)[-1]
        return res
    
    def coordenadaMenorOrdenada(self):
        res = []
        if(self.coordenadas == []):
            res = [0,0]
        else:
            res = sorted(self.coordenadas, key = lambda
                       coordenada: coordenada.y)[0]
        return res
    
    def getCaminos(self):
        res = []
        camino1 = []
        camino2 = []
        posMenorAbscisa = self.coordenadas.index(self.coordenadaMenorAbscisa())
        posMayorAbscisa = self.coordenadas.index(self.coordenadaMayorAbscisa())
        #Construcion de los dos caminos desde la coordenada de menor
        #abscisa a la de mayor.
        if posMenorAbscisa < posMayorAbscisa:
            camino1.extend(self.coordenadas[posMenorAbscisa:posMayorAbscisa+1])
            camino2.extend(self.coordenadas[posMayorAbscisa:])
            camino2.extend(self.coordenadas[:posMenorAbscisa+1])
        else:
            camino1.extend(self.coordenadas[posMayorAbscisa:posMenorAbscisa+1])
            camino2.extend(self.coordenadas[posMenorAbscisa:])
            camino2.extend(self.coordenadas[:posMayorAbscisa+1])
        #Ordenar caminos, ambos de izquierda a derecha.
        if not camino1[0].__equals__(self.coordenadaMenorAbscisa()):
            camino1.reverse()
        else:
            camino2.reverse()
        #Diferenciar cual es el superior e inferior.
        if (poligono(camino1[1:-1]).coordenadaMayorAbscisa().getY() 
            > poligono(camino2[1:-1]).coordenadaMayorAbscisa().getY()):
            res.append(camino1)
            res.append(camino2)
        else:
            res.append(camino2)
            res.append(camino1)
        return res
    
    def algoritmoDeLee(self):
        superior = []
        inferior = []
        LS = []
        LI = []
        res = []
        superior.extend(caminoLeeSuperior(self.getCaminos()[0], LS))
        inferior.extend(caminoLeeInferior(self.getCaminos()[1], LI))
        inferior.reverse()
        res.extend(superior)
        res.extend(inferior[1:-1])
        return poligono(res)
    
    def drawing(self):
        puntos = []
        for c in self.coordenadas:
            point = Point(c.getX(), c.getY())
            puntos.append(point)
        g = GraphWin("Drawing", 400, 400)
        g.setBackground("beige")
        maximaX = (self.coordenadaMayorAbscisa().getX() + 1).__abs__()
        maximaY = (self.coordenadaMayorOrdenada().getY() + 1).__abs__()
        minimaX = (self.coordenadaMenorAbscisa().getX() - 1).__abs__()
        minimaY = (self.coordenadaMenorOrdenada().getY() - 1).__abs__()
        g.setCoords(minimaX, minimaY, maximaX, maximaY)
        p = Polygon(puntos)
        p.setWidth(2)
        p.setOutline("blue")
        p.draw(g)
        time.sleep(4)
        g.close()
