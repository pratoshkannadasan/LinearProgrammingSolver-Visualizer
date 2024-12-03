from solver.lp_solver import solve_lp

def test_solve_lp():
    obj = [-1, -2]
    lhs_ineq = [[2, 1], [-4, 5], [1, -2]]
    rhs_ineq = [20, 10, 2]
    bounds = [(0, float('inf')), (0, float('inf'))]

    solution = solve_lp(obj, lhs_ineq, rhs_ineq, bounds)
    assert len(solution) == 2, 'Solution should have two variables'
