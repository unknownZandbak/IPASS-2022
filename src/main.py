import numpy as np
import itertools as it
from solver import solve

def generate_matrix(size: int) -> list: #! Deprecated use the new_generation_matrix function 
    """(Deprecated use the new_generation_matrix function)
    Generate a randomly filed  matrix of the given size
    Matrix will always be a square
    Args:
        size (int): Size of the wanted matrix e.g. 6 (6x6)

    Returns:
        list: returns a 2d numpy array wich acts as the matrix, and a accompanying list of imutable cell positions.
    """
    while 1:
        # generate a matrix of the given size
        shape = size, size
        # matrix = np.empty(shape)
        # matrix[:] = np.nan
        matrix = np.random.randint(1000, 9999, size=shape)
        # set the pre-set vallues amount, in this case its 20% of the matrix rounded down.
        rnd_amount = int(np.floor((len(matrix)**2)*.0))
        # A list of permanent value positions that are not allowed to be changed 
        permlist = []
        
        for i in range(rnd_amount):
            # randomly place a 1 or 0 in the matrix
            row = np.random.randint(0, len(matrix))
            column = np.random.randint(0, len(matrix.T))
            matrix[row,column] = np.random.randint(0, 2)
            # add a permanent value position to the list
            permlist.append((row, column))    

        if rule_checker(matrix)[0] == 0:
            return [matrix, permlist]

def new_generate_matrix(size: int):
    """Generate a randomly filed  matrix of the given size,
    Matrix will always be a square
    Args:
        size (int): Size of the wanted matrix e.g. 6 (6x6)

    Returns:
        list: returns a 2d numpy array wich acts as the matrix, and a accompanying list of imutable cell positions.
    """
    shape = size, size
    # First force the program to make a correct puzzle
    # while (rule_checker(matrix)[0] != 0) or (((matrix != 0) & (matrix != 1)).sum() != 0):
    matrix = np.random.randint(1000, 9999, size=shape)
    matrix = solve(matrix)
    
    # fille the matrix randomly with random numbers
    rnd_amount = int(np.floor((len(matrix)**2)*.95))
    for step in range(rnd_amount):
        row = np.random.randint(0, len(matrix))
        column = np.random.randint(0, len(matrix.T))
        matrix[row, column] = np.random.randint(1000, 10000)

    return matrix

def rule_checker(matrix: np.array) -> tuple:
    """Check for any conflicting rules for the given matrix.

    Args:
        matrix (np.array): Given matrix

    Returns:
        tuple: Returns a tuple of a error code and a message to tell what rule is conflicting
    """

    # * First rule is that no more then 2 of the same value's are allowed next to each other.
    for row in range(len(matrix)):
        for i in range(1, len(matrix)-1):
            if matrix[row,i-1] == matrix[row,i] == matrix[row,i+1]:
                return 1, "More then 2 consecutive values in a row"
    
    for column in range(len(matrix)):
        for i in range(1, len(matrix)-1):
            if matrix.T[column,i-1] == matrix.T[column,i] == matrix.T[column,i+1]:
                return 2, "More then 2 consecutive values in a column"

    # * Second rule is that there must be an equal amount of both values in a row an column.
    for row in matrix:
        c0 = 0
        c1 = 0
        for cell in row:
            if cell == 0:
                c0 += 1
            elif cell == 1:
                c1 += 1
        if c0 > len(row)/2 or c1 > len(row)/2:
            return 3, "Rows are unbalanced"

    for column in matrix.T:
        c0 = 0
        c1 = 0
        for cell in column:
            if cell == 0:
                c0 += 1
            elif cell == 1:
                c1 += 1
        if c0 > len(column)/2 or c1 > len(column)/2:
            return 4, "column are unbalanced"

    # * Third rule is that ther are now duplicate rows or columns allowed.
    for row in range(len(matrix)):
        Tb = matrix == matrix[row,:]
        Tb = Tb.all(1)
        Tb = np.delete(Tb, row)
        if True in Tb:
            return 5, "Rows are not unique"

    for column in range(len(matrix)):
        Tb = matrix.T == matrix.T[column,:]
        Tb = Tb.all(1)
        Tb = np.delete(Tb, column)
        if True in Tb:
            return 6, "Columns are not unique"

    # * if nothing is triggered then it would mean all rules are followed.
    return 0, "No conflicting rules"

def bruteforce(matrix: np.array) -> None: #! Dangerous Code Don't use
    """(Dangerous Code Don't use)Generates all possible matrices that follow the rules in the given matrix shape.
    Note 4x4 is easily doable but if you go to 6x6 then it will take a long time.

    Args:
        matrix (np.array): a matrix to get the wanted shape from.
    """
    size = len(matrix), len(matrix)
    prod = list(it.product(range(2), repeat=size[1]**2))

    for i in range(len(prod)):
        matrix = np.asarray(np.asarray(prod[i]).reshape((size)))

        if rule_checker(matrix)[0] == 0:
            print(f"======\nmatch found:\n{matrix}\n")

def editGrid(matrix_pak, pos=None, newVal=None) -> np.array:
    """Manualy edit the grid, meant to be use by the user with a input field

    Args:
        matrix_pak (_type_): matrix pakage
        pos (_type_, optional): position of changing value. Defaults to None.
        newVal (_type_, optional): new value to change cell to . Defaults to None.

    Returns:
        np.array: _description_
    """
    if pos == None:
        r = int(input("\nSelect Row: "))
        c = int(input("Select Column: "))
        pos = r, c
    
    if newVal == None:
        newVal = int(input("New Value: "))

    matrix, permList = matrix_pak
    if newVal != 1 and newVal != 0:
        return matrix, "Incorrect input value"
    else:
        # check if the given position is imutable
        if pos in permList:
            return matrix, "Cell has a immutable value"
        
        matrix[pos] = newVal
        # Verify that the value has correctly changed
        if matrix[pos] != newVal:
            return matrix, "Somthing went wrong when changing the value"

        return matrix, "Value changed correctly"

def manual_play(matrix: np.array):
    while (rule_checker(matrix)[0] != 0) or (((matrix != 0) & (matrix != 1)).sum() != 0):
        print(f"Puzzle: {matrix}")
        matrix = editGrid((matrix, ()))[0]

    print(f"Well done, U solved the puzzle :\n {matrix}")

def game_loop():

    input_size = 6
    print("\nGenerating Puzzle")
    matrix = new_generate_matrix(input_size)
    print(f"Generated Puzzle:\n{matrix}")

    while 1:
        print("""
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Choose one of the following Options:
N - Generate a new Puzzle
M - Manual Mode (manually fill in the puzzle)
A - Automated Mode (Let the programe itself solve the puzzle)
Q - Quit the programm
""")
        anwser = input(":: ")

        if anwser == "N" or  anwser == "n":
            input_size = int(input("Size of Puzzle: "))
            print("Generating Puzzle")
            matrix = new_generate_matrix(input_size)
            print(f"Generated Puzzle:\n{matrix}")
    
        elif anwser == "M" or anwser == "m": manual_play(matrix)
        elif anwser == "A" or anwser == "a": 
            print("Solving Puzzle")
            solved_matrix = solve(matrix)
            print(f"\n=====\nSolved Matrix:\n{solved_matrix}")
        elif anwser == "Q" or anwser == "q": break


if __name__ == '__main__' :
    
    game_loop()
    