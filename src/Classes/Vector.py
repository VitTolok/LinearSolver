from .Matrix import Matrix
class Vector:
    """A class for storing and operating Vectors.
    Mostly partial setup for future possible implementation of 
    more algorithms using vectors
    """
    def __init__(self, coordinates: list, base: Matrix = None):
        """Creates a new vector object given its coordinates and the base.
        Base defaults to an E matrix of the needed size, most operations 
        are conducted without base in mind, since there isn't a use for it yet
        Args:
            coordinates (list): the coordinates in a given(ortho by default) basis
            base (Matrix, optional): the basis. Defaults to None.
        Raises:
            Exception: Different number of dimensions in base and coordinates
        """
        self.__coords = list(map(complex, coordinates.copy()))
        if base is None:
            self.__base = Matrix([[1 if i == j else 0
                          for j in range(len(coordinates))]
                          for i in range(len(coordinates))])
        elif len(base.tolist())!=len(coordinates):
            raise Exception
        else:
            self.__base = base
    
    def __len__(self) -> int:
        """
        Returns:
            int: the number of coordinates
        """
        return len(self.__coords)
    
    def __sum__(self, other):
        """Vector sum, only supports the same basis vectors
        Args:
            other (Vector): The other Vector
        Raises:
            Exception: different bases
            Exception: not a vector
        Returns:
            Vector: the sum
        """
        if isinstance(other, Vector):
            if self.base() == other.base():
                return Vector([self.__coords[i] + other.__coords[i]
                               for i in range(len(self))])
            else:
                raise Exception
        else:
            raise Exception
    
    def __sub__(self, other):
        """Vector subtraction
        Args:
            other (Vector): the other Vector
        Raises:
            Exception: different basis
            Exception: not a Vector
        Returns:
            Vector: the result of subtraction
        """
        if isinstance(other, Vector):
            if self.base() == other.base():
                return Vector([self.__coords[i] - other.__coords[i]
                               for i in range(len(self))])
            else:
                raise Exception
        else:
            raise Exception

    def tobase(self, newbase: Matrix, transmat: Matrix):
        """Uses a transition matrix to change base
        Args:
            newbase (Matrix): the new base
            transmat (Matrix): the transition matrix
        Raises:
            Exception: transition matrix invalid
        """
        if newbase * transmat == self.__base:
            self = Vector([line[0] for line in transmat*self.tomatrix()], newbase)
        else:
            raise Exception

    def base(self) -> Matrix:
        """
        Returns:
            Matrix: a copy of its basis matrix
        """
        return self.__base.copy()
    
    def copy(self):
        """
        Returns:
            Vector: a copy of itself
        """
        return Vector(self.__coords.copy(), self.base())
        
    def tomatrix(self) -> Matrix:
        """
        Returns:
            Matrix: one column containing its coords
        """
        return Matrix([[coord] for coord in self.__coords.copy()])
    
    def tolist(self) -> list:
        """
        Returns:
            list: its coordinates
        """
        return self.__coords.copy()
    
    def is_ortho(self) -> bool:
        """
        Returns:
            bool: whether the basis is ortho
        """
        return (self.base() * self.tomatrix() == self.tomatrix())
    
    def to_ortho(self):
        """
        Returns:
            Vector: self in orthogonal unit basis
        """
        return Vector(line[0] for line in 
                      (self.base()*self.tomatrix()).tolist())
    