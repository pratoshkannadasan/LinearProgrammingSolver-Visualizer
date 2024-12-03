from solver.plot_visualizer import plot_lp

# Plotting test does not assert but ensures no runtime errors.
def test_plot_lp():
    obj = [-1, -2]
    lhs_ineq = [[2, 1], [-4, 5], [1, -2]]
    rhs_ineq = [20, 10, 2]
    bounds = [(0, 10), (0, 10)]
    solution = [2, 6]
    plot_lp(obj, lhs_ineq, rhs_ineq, bounds, solution)
