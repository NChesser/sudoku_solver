def cross(rows, digits):    
    return [row+digit for row in rows for digit in digits]

"""
Values for setting up a Sudoku Board
"""
digits = '123456789'
rows = 'ABCDEFGHI'
cols = digits

squares = cross(rows, digits)

unitlist = ([cross(rows, c) for c in cols] +
            [cross(r, cols) for r in rows] +
            [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')])

"""
Dictionary of all the squares and the squares associated with them
(the rows, colums and squares an individual square must be different from)
"""
squares_dict = {s:"0" for s in squares}
peers_dict = {s:set([p for l in unitlist for p in l if s in l]) for s in squares}

def get_moves(square, state):
    return set(set([d for d in digits]) - set([p for s in peers_dict[square] for p in state[s]]))

def is_goal(state):
    for s in state:
        if state[s] == "0":
            return False
    return True

def solve_sudoku(puzzle):
    return search(puzzle, state_sucessors, is_goal)

def search(start, successors, is_goal): 
    if is_goal(start):
        return start

    explored = set()
    frontier = [start]
    while frontier:
        path = frontier.pop()
        for state in successors(path):
            frontier.append(state)

        if is_goal(path):
            return path
        
    return False

def state_sucessors(state):
    """
    return all the possible valid states
    should return nothing if nothing is valid
    """
    states = []
    for s in state:
        if state[s] == "0":
            for n in get_moves(s, state):
                state2 = state.copy()   
                state2[s] = n
                states.append(state2)
            break     

    return states

def set_sudoku(string):
    values = [c for c in string] 
    for s in squares_dict:
        squares_dict[s] = values.pop(0)
    
    return squares_dict

def display_sudoku(values):
    for r in rows :
        for c in cols :
            print (values[r+c], end=' '), 
        print()
    print()

"""
Example Suduko puzzles 
"""
puz1 = "000260701680070090190004500820100040004602900050003028009300074040050036703018000"
puz2 = "100489006730000040000001295007120600500703008006095700914600000020000037800512004"
puz3 = "003020600900305001001806400008102900700000008006708200002609500800203009005010300"
puz4 = "000003017015009008060000000100007000009000200000500004000000020500600340340200000"

"""
Hard Sudoku designed to work against brute force
Maybe one day I'll use another method
"""
puz5 = "000000000000003085001020000000507000004000100090000000500000073002010000000040009"

display_sudoku(solve_sudoku(squares_dict))
display_sudoku(solve_sudoku(set_sudoku(puz1)))
display_sudoku(solve_sudoku(set_sudoku(puz2)))
display_sudoku(solve_sudoku(set_sudoku(puz3)))
display_sudoku(solve_sudoku(set_sudoku(puz4)))




