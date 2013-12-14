from Clases.Recta import *  

"""Caminos de Lee"""
def caminoLeeSuperior(camino, resCaminoLeeS):
    inicio = camino[0]
    resCaminoLeeS.append(inicio)
    if len(camino) > 1:
        lista = []
        pendiente = float('-inf')
        for c in camino[1:]:
            if not (c.getY() < inicio.getY() and
                c.getX() < inicio.getX()):
                pendActual =  recta(inicio, c).getPendiente()
                posicion = camino.index(c)
                if pendActual == pendiente:
                    lista.append(c)
                    pos = posicion
                elif pendActual > pendiente:
                    lista = []
                    lista.append(c)
                    pendiente = pendActual
                    pos = posicion
        resCaminoLeeS.extend(lista[:-1])
        caminoLeeSuperior(camino[pos:], resCaminoLeeS)
    return resCaminoLeeS

def caminoLeeInferior(camino, resCaminoLeeI):
    inicio = camino[0]
    resCaminoLeeI.append(inicio)
    if len(camino) > 1:
        lista = []
        pendiente = float('inf')
        for c in camino[1:]:
            if not (c.getY() > inicio.getY() and
                c.getX() < inicio.getX()):
                pendActual =  recta(inicio, c).getPendiente()
                posicion = camino.index(c)
                if pendActual == pendiente:
                    lista.append(c)
                    pos = posicion
                if pendActual <= pendiente:
                    lista = []
                    lista.append(c)
                    pendiente = pendActual
                    pos = posicion
        resCaminoLeeI.extend(lista[:-1])
        caminoLeeInferior(camino[pos:], resCaminoLeeI)
    return resCaminoLeeI
