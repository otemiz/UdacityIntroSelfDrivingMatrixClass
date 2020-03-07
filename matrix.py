import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        if (self.h == 1 and self.w == 1):
            return self.g[0][0]
        elif(self.h == 2 and self.w == 2):
            a = self.g[0][0]
            b = self.g[0][1]
            c = self.g[1][0]
            d = self.g[1][1]
            det = (a * d - b * c)
        return det

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")
        else:
            trace = 0
        # TODO - your code here
            for i in range(self.h):
                trace = trace + self.g[i][i]
            return trace
                    

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")
        inverse = []
        if (self.is_square() and self.h < 3):
            if self.h == 1:
                inverse.append([1/self.g[0][0]])
                return Matrix(inverse)
            elif self.h == 2:
                a = self.g[0][0]
                b = self.g[0][1]
                c = self.g[1][0]
                d = self.g[1][1]
            
                factor = 1/self.determinant()
            
                inverse = [[d, -b],[-c, a]]
                
                for i in range(self.h):
                    for j in range(self.w):
                        inverse[i][j] = factor * inverse[i][j]
                return Matrix(inverse)
            

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        matrix_transpose = []
        
        for i in range(self.w):
            new_row = []
            for j in range(self.h):
                new_row.append(self.g[j][i])
            matrix_transpose.append(new_row)
        
        return Matrix(matrix_transpose)

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        else:
            new =[]
            for i in range(self.h):
                row=[]
                for j in range(self.w):
                    row.append(self.g[i][j] + other.g[i][j])
                new.append(row)
            return Matrix(new)
                
                

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
        new =[]
        for i in range(self.h):
            row=[]
            for j in range(self.w):
                row.append(-self.g[i][j])
            new.append(row)
        return Matrix(new)

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        else:
            new =[]
            for i in range(self.h):
                row=[]
                for j in range(self.w):
                    row.append(self.g[i][j] - other.g[i][j])
                new.append(row)
            return Matrix(new)

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        m_rows = len(self.g)
        p_columns = len(other.g[0])
    
        result = []

        for r in range(m_rows):
            row_result = []
            rowA = self.get_row(r)

            for c in range(p_columns):
                colB = other.get_column(c)
                dot_prod = rowA.dot_product(colB)
                row_result.append(dot_prod)

            result.append(row_result)

        return Matrix(result)
        
        
    def get_row(self, row):
        return Matrix([self.g[row]])
    
    def get_column(self, column_number):
        column = []
        for r in range(len(self.g)):
            column.append(self.g[r][column_number])

        return Matrix([column])
    
    def dot_product(self, other):
        result = 0
        for i in range(0,len(self.g[0])):
            a = self.g[0][i]
            b = other.g[0][i]
            result = result + a*b            

        return result
        

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        
        new =[]
        for i in range(self.h):
            row=[]
            for j in range(self.w):
                row.append(self.g[i][j]*other)
            new.append(row)
        return Matrix(new)
    
        if isinstance(other, numbers.Number):
            pass
            #   
            # TODO - your code here
            #
            