'''
Created on 08/12/2013

@author: Felix
'''
import time
from Clases.Poligono import *
from Util.UtilesPoligono import *
from Util.Triangulacion import *
"""Poligono 1"""
l = []
c4 = coordenada(4,6)
c5 = coordenada(5,5)
c6 = coordenada(4,4)
c7 = coordenada(6,2)
c8 = coordenada(1,9)
c9 = coordenada(2,8)
c1 = coordenada(1,2)
c2 = coordenada(2,4)
c3 = coordenada(1,5)
l.append(c4)
l.append(c5)
l.append(c6)
l.append(c7)
l.append(c1)
l.append(c2)
l.append(c3)
l.append(c8)
l.append(c9)
p = poligono(l)
"""Poligono 2"""
l2 = []
cc4 = coordenada(4,6)
cc5 = coordenada(5,8)
cc6 = coordenada(6,4)
cc7 = coordenada(6,6)
cc8 = coordenada(7,1)
cc9 = coordenada(5,3)
cc1 = coordenada(4,2)
cc2 = coordenada(3,3)
cc3 = coordenada(3,4)
cc10 = coordenada(4,4)
cc11 = coordenada(7,6)
cc12 = coordenada(6, 2.5)
cc13 = coordenada(3.5,3)
l2.append(cc4)
l2.append(cc5)
l2.append(cc6)
l2.append(cc7)
l2.append(cc11)
l2.append(cc12)
l2.append(cc8)
l2.append(cc9)
l2.append(cc1)
l2.append(cc13)
l2.append(cc2)
l2.append(cc3)
l2.append(cc10)
p2 = poligono(l2)
pLee2 = p2.algoritmoDeLee()
p2Ord =ordenaPoligono(p2)
"""Prueba"""
p.drawing()
listaP = []
listaP.append(p2Ord)
listaP.append(pLee2)
listaP.extend(getBolsas(p2Ord))
#posicionamientoDraw(listaP)
cc = coordenada(1.5,4)
print(estaDentro(cc, p))

