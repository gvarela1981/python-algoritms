def make_matrix(relations):
    """
    Create a 2d matrix (dictionary filled with lists) from key:value lists
    input: list of 2 itmes list
           example 1: [['Carlos', 'Luis'], ['Maria', 'Luis], ['Carlos', 'Jenny']]
           example 2: [[1, 2], [2, 3], [4, 3]]
    output: 2d matrix (dictionary) where keys are the first element of every input list
           example 1: {'Carlos':['Luis', 'Jenny'], 'Maria':['Luis']}
           example 2: {1:[2], 2:[3], 4:[3]}
    """
    matrix = {}
    for relation in relations:
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


def remove_list_duplicates(listed_values):
    """
    Given a list of values with duplicates return a list with no duplicates
    List may come from a from values of a matrix
    """
    response_list = []
    for value in listed_values:
        if value not in response_list:
            response_list.append(value)
    return response_list
