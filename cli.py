from sympy import symbols, Eq, solve, sympify

print("Enter your Equation:")
y = input()

# Split the input string into left-hand side and right-hand side
lhs, rhs = y.split('=')

# Define the variable
x = symbols('x')

# Parse the left-hand side and right-hand side into SymPy expressions
lhs_expr = sympify(lhs)
rhs_expr = sympify(rhs)

# Create a SymPy equation
equation = Eq(lhs_expr, rhs_expr)

# Solve the equation
solution = solve(equation, x)
print("x =", solution)