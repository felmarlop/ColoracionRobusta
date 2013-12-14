'''
Created on 05/12/2013

@author: Felix
'''
from ColoracionRobusta import *
colores = ["Rojo", "Verde"]
"""Ejemplo 2"""
av2 = vertice("a")
bv2 = vertice("b")
cv2 = vertice("c")
dv2 = vertice("d")
ev2 = vertice("e")
a2 = arista(av2,bv2,5)
b2 = arista(av2,cv2,25)
c2 = arista(av2,dv2,25)
d2 = arista(av2,ev2,1)
e2 = arista(bv2,cv2,25)
f2 = arista(bv2,dv2,25)
g2 = arista(bv2,ev2,5)
h2 = arista(cv2,ev2,1)
i2 = arista(dv2,ev2,25)
g2 = grafo([a2, b2, c2, d2, e2, f2, g2, h2, i2])
print("\n===Ejemplo2===")
iniciog2 = time.time()
solucion = coloracionRobusta(g2, colores)
pprint.pprint(solucion[0])
print("Peso optimo: "+str(solucion[1]))
fing2 = time.time()
print("Tiempo de ejecucion: "+str(fing2 - iniciog2))