import numpy as np
import itertools as it

def generate_matrix(size: int) -> np.array:
    while 1:
        shape = size, size
        matrix = np.random.randint(1000, 9999, size=shape)
        rnd_amount = int(np.floor((len(matrix)**2)*.2))

        for i in range(rnd_amount):
            row = np.random.randint(0, len(matrix))
            column = np.random.randint(0, len(matrix.T))
            matrix[row,column] = np.random.randint(0, 2)
                
        if rule_checker(matrix)[0] == 0:
            return matrix

def rule_checker(matrix: np.array) -> tuple:
    """Check for any conflicting rules for the given matrix.

    Args:
        matrix (np.array): Given matrix

    Returns:
        tuple: Returns a tuple of a error code and a message to tell what rule is conflicting
    """
    # * First rule is that ther are now duplicate rows or columns allowed.
    for row in range(len(matrix)):
        Tb = matrix == matrix[row,:]
        Tb = Tb.all(1)
        Tb = np.delete(Tb, row)
        if True in Tb:
            return 1, "Rows are not unique"

    for column in range(len(matrix)):
        Tb = matrix.T == matrix.T[column,:]
        Tb = Tb.all(1)
        Tb = np.delete(Tb, column)
        if True in Tb:
            return 2, "Columns are not unique"

    # * Second rule is that no more then 2 of the same value's are allowed next to each other.
    # First we go through Rows then we go through the columns
    for row in range(len(matrix)):
        for i in range(1, len(matrix)-1):
            if matrix[row,i-1] == matrix[row,i] == matrix[row,i+1]:
                return 3, "More then 2 consecutive values in a row"
    
    for column in range(len(matrix)):
        for i in range(1, len(matrix)-1):
            if matrix.T[column,i-1] == matrix.T[column,i] == matrix.T[column,i+1]:
                return 4, "More then 2 consecutive values in a row"

    # * Third rule is that there must be an equal amount of both values in a row an column.
    for row in matrix:
        c0 = 0
        c1 = 0
        for cell in row:
            if cell == 0:
                c0 += 1
            elif cell == 1:
                c1 += 1
        if c0 > len(row)/2 or c1 > len(row)/2:
            return 5, "Rows are unbalanced"

    for column in matrix.T:
        c0 = 0
        c1 = 0
        for cell in column:
            if cell == 0:
                c0 += 1
            elif cell == 1:
                c1 += 1
        if c0 > len(column)/2 or c1 > len(column)/2:
            return 6, "column are unbalanced"


    # * if nothing is trigerd then it would mean all rules are followed and the matrix would be complete
    return 0, "No conflicting rules"

def bruteforce(matrix: np.array):
    size = len(matrix), len(matrix)
    prod = list(it.product(range(2), repeat=size[1]**2))

    for i in range(len(prod)):
        matrix = np.matrix(np.asarray(prod[i]).reshape((size)))

        if rule_checker(matrix)[0] == 0:
            print(f"======\nmatch found:\n{matrix}\n")

if __name__ == '__main__' :

    m4 = generate_matrix(4)
    # print(m4)
    # print(m4)
    bruteforce(m4)