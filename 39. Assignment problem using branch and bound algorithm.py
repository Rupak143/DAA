import sys
def reduce_matrix(matrix):
    n = len(matrix)
    for i in range(n):
        min_val = min(matrix[i])
        matrix[i] = [val - min_val for val in matrix[i]]
    for j in range(n):
        min_val = min(matrix[i][j] for i in range(n))
        for i in range(n):
            matrix[i][j] -= min_val         
    return matrix
def branch_and_bound_assignment(cost_matrix):
    n = len(cost_matrix)
    min_cost = sys.maxsize
    min_assignment = None
    def backtrack(assignment, total_cost, assigned_rows):
        nonlocal min_cost, min_assignment
        if len(assignment) == n:
            if total_cost < min_cost:
                min_cost = total_cost
                min_assignment = assignment.copy()
            return
        for col in range(n):
            if col not in assigned_rows:
                potential_cost = total_cost + cost_matrix[len(assignment)][col]
                if potential_cost < min_cost:
                    backtrack(assignment + [(len(assignment), col)], potential_cost, assigned_rows + [col])
    reduced_matrix = reduce_matrix(cost_matrix)
    backtrack([], 0, [])
    return min_assignment, min_cost
cost_matrix = [[5, 4, 2, 7],
               [2, 1, 5, 6],
               [4, 3, 2, 1],
               [3, 2, 1, 4]]
assignment, min_cost = branch_and_bound_assignment(cost_matrix)
print("Minimum cost of assignment:", min_cost)
print("Assignment:", assignment)
