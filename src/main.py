import numpy as np

def rule_checker(matrix):

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
    # First we go through Rows the we go through the columns
    pass

    # Now we go through the columns
    pass

    # * Third rule is that there must be an equal amount of both values in a row an column.
    for row in matrix:
        unique, frequency = np.unique(row, return_counts=True)
        if frequency[0] != frequency[1]:
            return 0, "Rows not in balance"
        
    for column in matrix.T:
        unique, frequency = np.unique(column, return_counts=True)
        if frequency[0] != frequency[1]:
            return 0, "Columns not in balance" 

if __name__ == '__main__' :

    shape = width, height = 6,6

    matrix = np.empty(shape)
    matrix = np.matrix(matrix)

    print(matrix)
      