import streamlit as st
from solver.lp_solver import solve_lp
from solver.multi_obj_solver import solve_multi_obj_lp
from solver.sensitivity_analysis import perform_sensitivity_analysis
from visualizer.plot_visualizer import plot_lp, plot_sensitivity_analysis
from visualizer.report_generator import generate_report
import json

def load_problem_from_file(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def save_problem_to_file(problem, filename):
    with open(filename, 'w') as f:
        json.dump(problem, f)

def main():
    st.title('Linear Programming Solver and Visualizer')

    # Upload problem JSON or manually input the problem
    uploaded_file = st.file_uploader("Upload problem (JSON)", type="json")
    if uploaded_file:
        problem = load_problem_from_file(uploaded_file)
    else:
        obj = st.text_input("Objective Function (comma separated, e.g., '3,-4')")
        constraints = []
        num_constraints = st.number_input("Number of Constraints", min_value=1)
        for i in range(num_constraints):
            lhs = st.text_input(f"Left-hand Side for Constraint {i+1} (comma separated)")
            rhs = st.text_input(f"Right-hand Side for Constraint {i+1}")
            constraints.append((lhs, rhs))

        problem = {
            'objective': obj,
            'constraints': constraints
        }

    # Solve problem
    if st.button("Solve"):
        solution = solve_lp(problem)
        st.write("Solution: ", solution)
        plot_lp(problem, solution)
        generate_report(problem, solution)

    # Multi-objective optimization (if enabled)
    if st.button("Solve Multi-Objective"):
        solution = solve_multi_obj_lp(problem)
        st.write("Pareto Front: ", solution)
        plot_lp(problem, solution)
        generate_report(problem, solution)

    # Sensitivity Analysis
    if st.button("Perform Sensitivity Analysis"):
        sensitivity_results = perform_sensitivity_analysis(problem)
        plot_sensitivity_analysis(sensitivity_results)

if __name__ == '__main__':
    main()



