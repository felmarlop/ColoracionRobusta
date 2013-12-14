"""
Objeto: Recta
Atributos: Dos coordenadas
"""
from Clases.Coordenada import *

class recta():
    a = coordenada
    b = coordenada
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def getA(self):
        return self.a
    
    def getB(self):
        return self.b
    
    def getPendiente(self):
        numerador = float(self.b.getY() - self.a.getY())
        denominador = float(self.b.getX() - self.a.getX())
        res = 0
        if denominador == 0:
            if numerador < 0:
                res = float('-inf')
            if numerador > 0:
                res = float('inf')
        else:
            res = round(numerador/denominador, 3)
        return res
    
    def __repr__(self):
        return self.a+" - "+self.b
    
    