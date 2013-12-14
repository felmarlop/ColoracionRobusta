'''
Created on 05/12/2013

@author: Felix
'''
from ColoracionRobusta import *
"""Vertices"""
av = vertice("a")
bv = vertice("b")
cv = vertice("c")
dv = vertice("d")

"""Aristas"""
a = arista(av,bv,10)
b = arista(av,cv,3)
c = arista(cv,dv,6)
d = arista(bv,dv,1)
e = arista(bv,cv,2)

"""Colores"""
colores = ["Rojo", "Verde"]

"""Grafo: lista de aristas"""
g1 = grafo([a, b, c, d, e])
print("===Ejemplo1===")
iniciog1 = time.time()
solucion = coloracionRobusta(g1, colores)
pprint.pprint(solucion[0])
print("Peso optimo: "+str(solucion[1]))
fing1 = time.time()
print("Tiempo de ejecucion: "+str(fing1 - iniciog1))