class Solver:
    """Abstract class for calculating algorithms
    the methods defined here manage inputs"""

    def __init__(self, input_list: list):
        self._input = input_list.copy()

    def setinput(self, value, index):
        self._input[index] = value

    def getinput(self, index):
        return self._input[index]

    def get_solution(self):
        """returns the result of calculations"""
        pass
