n_case1 = 2
case1 = "1 2"
# output 2, there's two people and 2 is the judge

n_case2 = 3
case2 = "1 3, 2 3"
# output 3, there's 3 people and 3 is the judge

n_case3 = 4
case3 = "1 3, 2 3, 3 1"
# output -1, there's 4 people but people 3 don't trust everybody

n_case4 = 4
case4 = "1 3, 2 3, 3 1, 4 3"
# output -1, there's 4 people but people 3 trust people 1 and it shouldn't trust no one

n_case5 = 4
case5 = "1 3, 2 3, 4 3"
# output 3, there's 4 people and people 3 is the judge


n = n_case5
str_relations = case5

trust = [[int(val) for val in pair.split()] for pair in str_relations.strip().split(',')]

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

    def check_criteria1(trust_matrix):
        """ 
        returns the number representing people who trust no one (criteria 1)
        when only one person trust no one, return False otherwise 
        """
        judge_candidates = []
        town_people = get_matrix_keys(trust_matrix)
        # People will take numbers from 1 to n 
        # town people will trust every town people, so they will have a 
        # key in the matrix and a list of trusted people
        # judge_candidate will have no list of trusted people
        # only one person can fit this criteria
        for candidate in range(1, n+1):
            if candidate not in town_people: judge_candidates.append(candidate)
        response = judge_candidates[0] if len(judge_candidates) == 1 else None
        return response
    
    def check_criteria2(candidate_judge, trust_matrix):
        """ returns True if town people meets criteria 2, False if it doesn't"""
        town_people_trust_matrix = trust_matrix.pop(candidate_judge) if candidate_judge in trust_matrix.keys() else trust_matrix
        town_people_meets_criteria = True
        town_people_matrix_keys = list(town_people_trust_matrix.keys())
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
    # Check if candidate is the judge
    is_judge = False if judge_candidate is None else check_criteria2(judge_candidate, trust_matrix)
    response = -1 if is_judge == False else judge_candidate
    return response


print(get_judge(n, trust))