import sympy as sp  # pip install sympy

def solve_equation(equation, variable):
    equation = equation.replace('=', '-(') + ')'
    eq = sp.sympify(equation)
    solutions = sp.solve(eq, variable)
    return solutions


if __name__ == "__main__":
    x = sp.symbols('x')
    equation = input("Enter the equation to solve (e.g., 'x**2 - 4 = 0'): ")
    solutions = solve_equation(equation, x)
    print(f"Solutions: {solutions}")
