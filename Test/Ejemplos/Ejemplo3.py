'''
Created on 05/12/2013

@author: Felix
'''
from ColoracionRobusta import *

print("\n===Ejemplo3===")
av3 = vertice("a")
bv3 = vertice("b")
cv3 = vertice("c")
dv3 = vertice("d")
ev3 = vertice("e")
fv3 = vertice("f")
gv3 = vertice("g")
hv3 = vertice("h")
a3 = arista(av3,bv3,4)
b3 = arista(av3,cv3,2)
c3 = arista(av3,fv3,6)
d3 = arista(av3,gv3,8)
e3 = arista(av3,hv3,7)
f3 = arista(bv3,cv3,5)
g3 = arista(bv3,dv3,6)
h3 = arista(bv3,ev3,5)
i3 = arista(bv3,gv3,6)
j3 = arista(cv3,dv3,4)
k3 = arista(cv3,ev3,3)
l3 = arista(dv3,ev3,4)
m3 = arista(dv3,fv3,5)
n3 = arista(ev3,fv3,4)
o3 = arista(ev3,gv3,5)
p3 = arista(fv3,gv3,3)
q3 = arista(fv3,hv3,7)
r3 = arista(gv3,hv3,4)
colores2 = ["Rojo", "Verde", "Azul"]
g3 = grafo([a3, b3, c3, d3, e3, f3, g3, h3, i3, j3, k3, l3, m3, n3, o3, p3, q3, r3])
iniciog3 = time.time()
solucion = coloracionRobusta(g3, colores2)
pprint.pprint(solucion[0])
print("Peso optimo: "+str(solucion[1]))
fing3 = time.time()
print("Tiempo de ejecucion: "+str(fing3 - iniciog3))
