from Clases.Recta import *

"""Metodo que comprueba si un punto esta dentro de un poligono o no"""
def estaDentro(a,l_poly):
    n = len(l_poly.getCoordenadas())
    inside =False
    j = 0
    for i in range(n):
        j+=1
        if (j == n):
            j = 0
        if (l_poly.getCoordenadas()[i].getY() < a.getY() and l_poly.getCoordenadas()[j].getY() >= a.getY() or l_poly.getCoordenadas()[j].getY() < a.getY() and l_poly.getCoordenadas()[i].getY() >= a.getY()):
            if (l_poly.getCoordenadas()[i].getX() + (a.getY() - l_poly.getCoordenadas()[i].getY()) / (l_poly.getCoordenadas()[j].getY() - l_poly.getCoordenadas()[i].getY()) * (l_poly.getCoordenadas()[j].getX() - l_poly.getCoordenadas()[i].getX()) < a.getX()):
                inside = not inside
    return inside
        
    
    
    