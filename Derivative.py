import sympy as sp

# Define the variable and the function
x = sp.symbols('x')
function_str = input("Enter a function in terms of 'x': ")

# Parse the user input to create the function
try:
    function = sp.sympify(function_str)
except sp.SympifyError:
    print("Invalid input. Please enter a valid function.")
    exit(1)

# Calculate the integral
integral = sp.integrate(function, x)

# Print the result
print(f"Original function: {function}")
print(f"Integral: {integral} + C")  # Add the constant of integration 'C'
