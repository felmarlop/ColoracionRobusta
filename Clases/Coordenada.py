"""
Objeto: Coordenada
Atributos: X e Y
"""
class coordenada():
    def  __init__(self, x, y):
        self.x = x
        self.y = y
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def __equals__(self, other):
        return (self.x, self.y) == (other.x, other.y)
    
    def __repr__(self):
        return "("+str(self.x)+","+str(self.y)+")"