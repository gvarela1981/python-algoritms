n_case10 = 2
case10 = [['Carlos', 'Luis']]
# output Luis, there is two people and everyboyd meets criteria

n_case11 = 2
case11 = [['Carlos', 'Luis'], ['Maria', 'Luis'], ['Claudia', 'Luis']]
# output -1, there is more people than indicated. Claudia is number 4 and Luis is number 3 of only 2 people

n_case12 = 4
case12 = [['Carlos', 'Luis'], ['Maria', 'Luis'], ['Claudia', 'Luis']]
# output Luis, there is 4 people and everybody meets criteria

n_case13 = 4
case13 = [['Carlos', 'Luis'], ['Maria', 'Luis'], ['Claudia', 'Luis'], ['Luis', 'Carlos']]
# output -1, there is 4 people but nobody meets criteria 1

n_case14 = 4
case14 = [['Carlos', 'Luis'], ['Maria', 'Luis']]
# output -1, there is less people than indicated, meaning someone don't meet criteria 2

n = n_case10
trust = case10

def make_matrix(relations):
    """
    Create a matrix from key:value lists
    input: list of 2 itmes list
           example: [['Carlos', 'Luis'], ['Maria', 'Luis], ['Carlos', 'Jenny']]
    output: 2d matrix where index are the first element of every input list
           example: {'Carlos':['Luis', 'Jenny'], 'Maria':['Luis']}
    """
    matrix = {}
    for relation in relations:
        trusting = relation[0]
        trusted = relation[1]
        try:
            matrix[trusting].append(trusted)
        except KeyError as e:
            matrix.update({trusting: [trusted]})
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


def remove_list_duplicates(list):
    """
    Given a list of values with duplicates return a list with no duplicates
    List may come from a from values of a matrix
    """
    response_list = []
    for value in list:
        if value not in response_list:
            response_list.append(value)
    return response_list


def get_judge(n, trust):
    """
    Returns -1 if is not possible to find only 1 person meeting judge criteria
    Returns the number of the person who is distinctly a judge
    Criteria1: town judge trust nobody
    Criteria2: everybody (except the judge) trust the town judge
    Criteria3: only one person can meet criteria 1 and 2

    input:  n (number)
            trust (string) "number1 number2, number3 number3, ..."
    output: number of person meeting judge criteria
            -1 if no person (or more than one) meet judge criteria
    """

    def check_criteria1(matrix):
        """ 
        returns the one person meeting criteria 1 or None if there is None or more than one.
        people represented as a key in the matrix represent someone who trust in
        the people represented as values for that key

        people who trust no one will have no key in the matrix

        validation should consider the number of people n
        only n-1 people can trus nobody, so n-1 people should have a key in matrix
        no more and no less
        """
        # Only one people can trust no one, there should be n -1 people trusting others
        if len(get_matrix_keys(matrix)) != n - 1: return -1

        # Now we check there's only 1 candidate for judge, let's find out the name
        # make a list of all values in the matrix (matrix_values), 
        # the ones present as keys  and the ones that are not (no duplicates)
        matrix_keys = get_matrix_keys(matrix)
        candidates = get_matrix_single_values_and_keys(matrix)
        # remove al people who trust someone, that is the ones who has a key in matrix 
        # in the end there should be just one candidate in candidates
        for candidate in matrix_keys:
            if candidate in candidates:
                candidates.remove(candidate)
        return candidates[0]
    
    def check_criteria2(candidate_judge, trust_matrix):
        """ returns True if town people meets criteria 2, False if it doesn't"""
        town_people_trust_matrix = trust_matrix.pop(candidate_judge) if candidate_judge in trust_matrix.keys() else trust_matrix
        town_people_meets_criteria = True # until proven otherwise
        town_people_matrix_keys = get_matrix_keys(town_people_trust_matrix)
        for i in range(len(town_people_trust_matrix)):
            key = town_people_matrix_keys[i]
            if candidate_judge not in town_people_trust_matrix[key]:
                #If one town people don't trust judge_candidate then candidate is not judge
                town_people_meets_criteria = False
                break
        response = True if town_people_meets_criteria else False
        return response


    trust_matrix = make_matrix(trust)
    judge_candidate = (check_criteria1(trust_matrix))
    # Check if candidate(s) is/are judge, check only one at a time
    is_judge = False if judge_candidate is None else check_criteria2(judge_candidate, trust_matrix)
    response = -1 if is_judge == False else judge_candidate
    return response

print(get_judge(n, trust))