def make_hash_table_collection(relations):
    """
    Create a 2d matrix (dictionary filled with lists) from key:value lists
    input: list of 2 itmes list
           example 1: [['Carlos', 'Luis'], ['Maria', 'Luis], ['Carlos', 'Jenny']]
           example 2: [[1, 2], [2, 3], [4, 3]]
    output: 2d matrix (dictionary) where keys are the first element of every input list
           example 1: {'Carlos':['Luis', 'Jenny'], 'Maria':['Luis']}
           example 2: {1:[2], 2:[3], 4:[3]}
    """
    hash_table_collection = {}
    for relation in relations:
        row = relation[0]
        col = relation[1]
        try:
            hash_table_collection[row].append(col)
        except KeyError as e:
            hash_table_collection.update({row: [col]})
    return hash_table_collection


def get_hash_table_collection_keys(hash_table_collection):
    """ Return al keys from matrix """
    return list(hash_table_collection.keys())


def get_hash_table_single_values_and_keys(hash_table_collection):
    """
    Return a list of all values in hash_table_collection, columns and rows
    values are not duplicated
    
    input: dictionary with 2d hash_table_collection
    output: list
    """
    hash_table_collection_keys = get_hash_table_collection_keys(hash_table_collection).copy()
    hash_table_collection_values = hash_table_collection_keys.copy()
    for row in hash_table_collection_keys:
        for value in hash_table_collection[row]:
            if value not in hash_table_collection_values: hash_table_collection_values.append(value)
    return hash_table_collection_values


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


def get_vertical_string(hash_table_collection, col):
    """
    Return the list of values fot the requested column number
    None when hash_table_collection has no value at this column
    """
    keys = list(hash_table_collection.keys())
    if col == 0: return keys
    response = []
    for row in keys:
      try:
        # First column is actually the index, colum 1 of the row 
        # becomes first element of the list -- hash_table_collection[row][col -1]
        response.append(hash_table_collection[row][col - 1]) 
      except IndexError as e:
        # If row has no value at this column set to None
        response.append(None)
    return response

def get_horizontal_string_by_index(hash_table_collection, row):
    """
    Return the list of values for the requested row number, the first value is the hash
    None when matrix has no value at this row
    """
    keys = list(hash_table_collection.keys())
    if row > len(keys) - 1: return None
    response = []
    # get hash_table_collection first colum (column 0) which is actually hash_table_collection[0]
    response.append(keys[row])
    # get matrix columns 1 to n for row "row"
    for col in range(len(hash_table_collection[keys[row]])):
      try:
        response.append(hash_table_collection[keys[row]][col]) 
      except IndexError as e:
        # If row has no value at this column set to None
        response.append(None)
    return response


def get_horizontal_string(hash_table_collection, hash):
    """
    Return the list of values for the requested has, the first value is the hash
    None when hash does not exists 
    """
    _hashes = list(hash_table_collection.keys())
    if hash not in _hashes: return None

    response = []
    # get hash table first colum (column 0) which is actually hash_table_collection[0]
    # hash_table_collection[1] or hash_table_collection['first'] or hash_table_collection['volvo']
    response.append(hash)
    # get hash table collection columns 1 to n for row "hash"
    for value in hash_table_collection[hash]:
      response.append(value)
    
    return response


def get_diagonal_string(hash_table_collection, direction='right', start_col=0, start_row=0, length=0):
  """
  Returns a list with a sequence of the values on a diagonal axis
  input:  matrix
          direction -> axis to iterate (right, left)
          start_col -> number of column to start the return sequence
          start_row -> value of the row to to start the return sequence
          start -> index number of the list to start the sequence to return (default zero)
          length -> index number ot the list to end the sequence to return (default last)
  output: a list with the values of the selected diagonal 
  """
  keys = list(hash_table_collection.keys())
  length = length if (isinstance(length, int) and length > 0) else len(keys)
  start_row_num = keys.index(start_row) if start_row in keys else 0
  end_row_num = start_row_num + length
  start_col_num = start_col if isinstance(start_col, int) else 0
  next_iteration = 1 if direction == 'right' else -1
  current_col_num = start_col_num # starts at start_col_num and increments during parsing
  response = []
  
  for row in keys[start_row_num:end_row_num]:
    try:
      value = hash_table_collection[row][current_col_num - 1] if current_col_num != 0 else row
      response.append(value)
    except IndexError as e:
      response.append(None) # If the hash table has no element at this position return none
    except Exception as e:
      print(f"Exception: {e}")
      pass
    current_col_num = current_col_num + next_iteration

  return response