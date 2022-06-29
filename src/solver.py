import numpy as np

def Backtrack_Based_Search(matrix, pos=None, new_val=None):
    # fill a empty cell and start the propagation again.
    if pos != None and new_val != None:
        print(pos, new_val)
        matrix[pos[0], pos[1]] = new_val
    matrix = Constraint_propagations(matrix)
    print(matrix)
    print("==========")

    if rule_checker(matrix)[0] != 0:
        return

    else:
        # Check if there are nomore empty cells 
        # Then return out of the function and return the solved matrix
        if ((matrix != 0) & (matrix != 1)).sum() == 0: 
            # print(matrix)
            return matrix

        # Else we take a random empty cell and fill it
        else:
            tmp_val = np.random.choice(matrix[(matrix != 0) & (matrix != 1)])
            x, y = np.where(matrix == tmp_val)
            pos = int(x), int(y)
            Backtrack_Based_Search(matrix, pos, 0)
            Backtrack_Based_Search(matrix, pos, 1)

def Constraint_propagations(matrix: np.array) -> np.array:

    changes = 1
    while changes:
        changes = 0

        # Constraint 1
        for row in range(len(matrix)):
            for i in range(1, len(matrix)-1):
                # Find combination of contraint satisfaction
                # Iterate Rows
                if ((matrix[row] != 0) & (matrix[row] != 1)).sum() > 0: # Check if there are any empty cells
                    if (matrix[row,i-1] == matrix[row,i]) and (matrix[row,i+1] != 1 and matrix[row,i+1] != 0):
                        matrix[row,i+1] = 0
                        if rule_checker(matrix)[0] == 0: pass
                        else: matrix[row,i+1] = 1
                        changes = 1

                    elif (matrix[row,i-1] == matrix[row,i+1]) and (matrix[row,i] != 1 and matrix[row,i] != 0):
                        matrix[row,i] = 0
                        if rule_checker(matrix)[0] == 0: pass
                        else: matrix[row,i] = 1
                        changes = 1
    
                    elif (matrix[row,i] == matrix[row,i+1]) and (matrix[row,i-1] != 1 and matrix[row,i-1] != 0):
                        matrix[row,i-1] = 0
                        if rule_checker(matrix)[0] == 0: pass
                        else: matrix[row,i-1] = 1
                        changes = 1


                # Iterate Columns
                if ((matrix.T[row] != 0) & (matrix.T[row] != 1)).sum() > 0: # Check if there are any empty cells
                    if (matrix[i-1,row] == matrix[i,row]) and (matrix[i+1,row] != 1 and matrix[i+1,row] != 0):
                        matrix[row,i+1] = 0
                        if rule_checker(matrix)[0] == 0: pass
                        else: matrix[row,i+1] = 1
                        changes = 1

                    elif (matrix[i-1,row] == matrix[i+1,row]) and (matrix[i,row] != 1 and matrix[i,row] != 0):
                        matrix[row,i] = 0
                        if rule_checker(matrix)[0] == 0: pass
                        else: matrix[row,i] = 1
                        changes = 1
    
                    elif (matrix[i,row] == matrix[i+1,row]) and (matrix[i-1,row] != 1 and matrix[i-1,row] != 0):
                        matrix[row,i-1] = 0
                        if rule_checker(matrix)[0] == 0: pass
                        else: matrix[row,i-1] = 1
                        changes = 1
            

        # Constraint 2
        for row in range(len(matrix)):
            if ((matrix[row] != 0) & (matrix[row] != 1)).sum() > 0: # Check if there are any empty cells
                # Iterate Rows
                if (matrix[row] == 0).sum() == len(matrix)//2:
                    matrix[row][(matrix[row] != 0) & (matrix[row] != 1)] = 1
                    changes = 1
                elif (matrix[row] == 1).sum() == len(matrix)//2: 
                    matrix[row][(matrix[row] != 0) & (matrix[row] != 1)] = 0
                    changes = 1

            if ((matrix.T[row] != 0) & (matrix.T[row] != 1)).sum() > 0: # Check if there are any empty cells
                # Iterate Columns
                if (matrix.T[row] == 0).sum() == len(matrix)//2:
                    matrix.T[row][(matrix.T[row] != 0) & (matrix.T[row] != 1)] = 1
                    changes = 1
                elif (matrix.T[row] == 1).sum() == len(matrix)//2: 
                    matrix.T[row][(matrix.T[row] != 0) & (matrix.T[row] != 1)] = 0
                    changes = 1

        # Constraint 3
        for row in range(len(matrix)-1):
            # Iterate Rows
            if ((matrix[row] != 0) & (matrix[row] != 1)).sum() == 0: # Check if there are no empty cells
                for row2 in range(row+1, len(matrix)):
                    if ((matrix[row2] != 0) & (matrix[row2] != 1)).sum() == 2: 

                        # Making masks to use for comparing the 2 arrays
                        filled_mask = ((matrix[row2] == 0) | (matrix[row2] == 1))
                        flipped_filled_mask = [not elem for elem in filled_mask]

                        # if the 2 array's are the same not looking at the non filled in part if the second row
                        if np.all(matrix[row][filled_mask] == matrix[row2][filled_mask]):

                            # get the values for the empty part from the first row
                            gap_values = matrix[row][np.where(filled_mask == False)[0]]
                            
                            # flip the values
                            flipped_gap_values = np.flip(gap_values)
                            
                            # and fill the second row
                            matrix[row2][flipped_filled_mask] = flipped_gap_values

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