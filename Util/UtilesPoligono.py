from Clases.Poligono import *
"""Devuelve el poligono que le pasamos como entrada
con las coordenadas ordenadas desde la de menor abscisa
a la mayor"""
def ordenaPoligono(p):
    res = []
    reverse = []
    res.extend(p.getCaminos()[0])
    reverse.extend(p.getCaminos()[1])
    reverse.reverse()
    res.extend(reverse[1:-1])
    p.setCoordenadas(res)
    return p

"""Bolsas de un poligono"""   
def getBolsas(p):
    pLee = p.algoritmoDeLee()
    res = []
    pFin = []
    ultimaP = p.getCoordenadas()[-1]
    ultimaPLee = pLee.getCoordenadas()[-1]
    for i in range(len(pLee.getCoordenadas())-1):
        c1 = pLee.getCoordenadas()[i]
        c2 = pLee.getCoordenadas()[i+1]
        indexC1 = p.getCoordenadas().index(c1)
        indexC2 = p.getCoordenadas().index(c2)
        if indexC2 -  indexC1 != 1:
            pRes = poligono(p.getCoordenadas()[indexC1:indexC2+1])
            res.append(pRes)
    if not ultimaP.__equals__(ultimaPLee):
        indexFinal = p.getCoordenadas().index(ultimaPLee)
        pFin.extend(p.getCoordenadas()[indexFinal:])
        pFin.append(p.getCoordenadas()[0])
        res.append(poligono(pFin))
    return res

"""Metodo que dibuja un conjunto de poligonos"""
def posicionamientoDraw(listaPoligonos):
    dibujos = []
    colores =  ["blue", "red"]
    for pol in listaPoligonos:
        puntos = []
        for c in pol.getCoordenadas():
            point = Point(c.getX(), c.getY())
            puntos.append(point)
        p = Polygon(puntos)
        p.setWidth(2)
        dibujos.append(p)
    maximaX = (listaPoligonos[0].coordenadaMayorAbscisa().getX() + 1).__abs__()
    maximaY = (listaPoligonos[0].coordenadaMayorOrdenada().getY() + 1).__abs__()
    minimaX = (listaPoligonos[0].coordenadaMenorAbscisa().getX() - 1).__abs__()
    minimaY = (listaPoligonos[0].coordenadaMenorOrdenada().getY() - 1).__abs__()
    g = GraphWin("Drawing", 400, 400)
    g.setBackground("beige")
    g.setCoords(minimaX, minimaY, maximaX, maximaY)
    for d2 in dibujos[2:]:
        d2.setFill("white")
        d2.draw(g)
    for d in dibujos[:2]:
        for color in colores:
            d.setOutline(color)
            colores.remove(color)
        d.draw(g)
    g.mainloop()
    
     


            
    
    