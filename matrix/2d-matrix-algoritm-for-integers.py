def make_matrix(list):
    """
    Create a 2d matrix (dictionary filled with lists) from key:value lists
    input: list of 2 itmes list
           example: [[1, 2], [2, 3], [4, 3]]
    output: 2d matrix where index are the first element of every input list
           example: {1:[2], 2:[3], 4:[3]}
    """
    matrix = {}
    for relation in list:
        row = relation[0]
        col = relation[1]
        try:
            matrix[row].append(col)
        except KeyError as e:
            matrix.update({row: [col]})
    return matrix


def get_matrix_keys(matrix):
    """ Return al keys from matrix """
    return list(matrix.keys())


def get_matrix_single_values_and_keys(matrix):
    """
    Return a list of all values in matrix, columns and rows
    values are not duplicated
    
    input: dictionary with 2d matrix
    output: list
    """
    matrix_keys = get_matrix_keys(matrix).copy()
    matrix_values = matrix_keys.copy()
    for row in matrix_keys:
        for value in matrix[row]:
            if value not in matrix_values: matrix_values.append(value)
    return matrix_values

