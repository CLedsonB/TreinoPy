#_________________METODO_1______________
class Cubo(object):
    result = 0
    
    def __init__(self, aresta):
        self.aresta = aresta
        
    def area(self):
        result = self.aresta ** 2
        return print(result)
        
    def volume(self):
        result = self.aresta ** 3
        return print(result)
        
c = Cubo(3)
c.area()
c.volume()

#________________METODO_2______________
class Cubo(object):
    result = 0
    
    def __init__(self, aresta):
        self.aresta = aresta
        
    def area(self):
        result = self.aresta ** 2
        return result
        
    def volume(self):
        result = self.aresta ** 3
        return result
        
c = Cubo(3)
print(c.area())
print(c.volume())