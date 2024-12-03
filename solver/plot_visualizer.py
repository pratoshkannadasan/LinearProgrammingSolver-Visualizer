import numpy as np
import matplotlib.pyplot as plt

def plot_lp(c, A_ub, b_ub, bounds, solution):
    fig, ax = plt.subplots()
    x = np.linspace(bounds[0][0], bounds[0][1], 400)
    for (a, b), rhs in zip(A_ub, b_ub):
        y = (rhs - a * x) / b
        ax.plot(x, y, label=f'{a}x + {b}y <= {rhs}')

    ax.scatter(solution[0], solution[1], color='red', label='Optimal Solution')
    ax.set_xlim(bounds[0])
    ax.set_ylim(bounds[1])
    ax.legend()
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    plt.title('Linear Programming Feasible Region')
    plt.grid(True)
    plt.show()
