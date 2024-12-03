from scipy.optimize import linprog

def solve_lp(c, A_ub, b_ub, bounds):
    result = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method='highs')
    if result.success:
        return result.x
    else:
        raise ValueError('No solution found!')
