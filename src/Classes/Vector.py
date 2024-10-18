from .Matrix import Matrix
class Vector:
    def __init__(self, coordinates: list, base: Matrix = None):
        self.__coords = list(map(complex, coordinates.copy()))
        if base is None:
            self.__base = Matrix([[1 if i == j else 0
                          for j in range(len(coordinates))]
                          for i in range(len(coordinates))])
        elif len(base.tolist())!=len(coordinates):
            raise Exception
        else:
            self.__base = base
    
    def __len__(self):
        return len(self.__coords)
    
    def __sum__(self, other):
        if isinstance(other, Vector):
            if self.base() == other.base():
                return Vector([self.__coords[i] + other.__coords[i]
                               for i in range(len(self))])
            else:
                raise Exception
        else:
            raise Exception

    def base(self):
            return self.__base.copy()
    
    def copy(self):
        return Vector(self.__coords.copy(), self.base())
        
    def tomatrix(self):
        return Matrix([[coord] for coord in self.__coords.copy()])
    
    def tolist(self):
        return self.__coords.copy()
    
    def is_ortho(self):
        return (self.base() * self.tomatrix() == self.tomatrix())
    
    def to_ortho(self):
        return Vector(line[0] for line in 
                      (self.base()*self.tomatrix()).tolist())
    