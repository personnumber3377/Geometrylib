import tkinter as tk
import sympy as sp
from tkinter import Text


def clean_input(x: str) -> list:
    temp = x.replace(' ', '').split('\n')
    cleaned = list(filter(None, temp))
    return cleaned


def create_res(x: str):
    split = x.split('=')
    res_eq = (sp.parse_expr(split[0], evaluate=False) - sp.parse_expr(split[1], evaluate=False))
    return res_eq


def define_eqsys_vars(eqsys: list):
    unique_vars = set()
    for eq in eqsys:
        unique_vars = unique_vars.union(eq.atoms(sp.Symbol))

    # create a list with all symbols converted to text, and join - var() takes a string
    var_string = ', '.join([repr(eq) for eq in unique_vars])
    variables = sp.var(var_string)
    return variables


def create_eqsys(x: list) -> tuple:
    equation_system = [create_res(eq) for eq in x]
    variables = define_eqsys_vars(equation_system)
    return equation_system, variables


def create_guess(eqsys: list) -> tuple:
    unique_vars = set()
    for eq in eqsys:
        unique_vars = unique_vars.union(eq.atoms(sp.Symbol))
    guess = [1] * len(unique_vars)
    return tuple(guess)


def solve_eqsys(eqsys, symbols, guess):
    result = sp.nsolve(tuple(eqsys), symbols, guess)
    return result


def main():
    # input, from tkinter window
    text_input = inputtxt.get("1.0", "end-1c")

    # clean text
    cleaned_text = clean_input(text_input)

    # create system of equations and try to solve it
    eqsys, eqsys_vars = create_eqsys(cleaned_text)
    guess = create_guess(eqsys)
    solution = solve_eqsys(eqsys, eqsys_vars, guess)

    # text output
    Output.insert(tk.END, f"Solution: {solution}")

    return 


# Build GUI
root = tk.Tk()
toplabel = tk.Label(text="Start variable name with a letter")
inputtxt = Text(root, height=30, width=50, bg="light yellow")
Output = Text(root, height=30, width=25, bg="light cyan")
Display = tk.Button(root, height=2,
                    width=20,
                    text="Solve system of equations",
                    command=lambda: main())
toplabel.pack()
inputtxt.pack()
Display.pack()
Output.pack()
tk.mainloop()