from traceback import print_tb
import numpy as np
import itertools as it

def generate_matrix(size) -> np.matrix:
    shape = size, size

    matrix = np.empty(shape, int)
    matrix = np.matrix(matrix)

    for row in range(len(matrix)):
        matrix[row]= np.random.random_integers(20,9999, len(matrix.T))

    return matrix

def rule_checker(matrix) -> tuple:
    # ! This implementation of the first rule is completely borked
    # * First rule is that ther are now duplicate rows or columns allowed.
    # Check for duplicates in the rows 
    unique, frequency = np.unique(matrix, return_counts=True)
    if 1 not in frequency:
        return 0, "Rows are not unique"
    
    # Check for duplicates in the collumns
    unique, frequency = np.unique(matrix.T, return_counts=True)
    if 1 not in frequency:
        return 0, "Columns are not unique"

    # * Second rule is that no more then 2 of the same value's are allowed next to each other.
    # First we go through Rows then we go through the columns
    for row in range(len(matrix)):
        for i in range(1, len(matrix)-1):
            if matrix[row,i-1] == matrix[row,i] == matrix[row,i+1]:
                return 0, "More then 2 consecutive values in a row"
    
    for column in range(len(matrix)):
        for i in range(1, len(matrix)-1):
            if matrix.T[column,i-1] == matrix.T[column,i] == matrix.T[column,i+1]:
                return 0, "More then 2 consecutive values in a row"

    # ! Third rule is also completly borked
    # ? Don't work with unique 
    # * Third rule is that there must be an equal amount of both values in a row an column.
    for row in matrix:
        unique, frequency = np.unique(row, return_counts=True)
        if frequency[0] != frequency[1]:
            return 0, "Rows not in balance"
        
    for column in matrix.T:
        unique, frequency = np.unique(column, return_counts=True)
        if frequency[0] != frequency[1]:
            return 0, "Columns not in balance" 

    # * if nothing is trigerd then it would mean all rules are followed and the matrix would be complete
    return 1, "No conflicting rules"

def bruteforce(matrix):
    size = len(matrix), len(matrix)
    prod = list(it.product(range(2), repeat=size[1]**2))

    for i in range(len(prod)):
        matrix = np.matrix(np.asarray(prod[i]).reshape((size)))

        if rule_checker(matrix)[0]:
            print(f"======\nmatch found:\n{matrix}\n")

if __name__ == '__main__' :

    m4 = generate_matrix(4)
    
    bruteforce(m4)