from functools import reduce
from fractions import Fraction



def find_gcf_two_numbers(a, b):
    while b:
        a, b = b, a % b
    return a





def factor_squares(equation):
    if not equation.contains("-"): return "prime"
    equation = equation.replace(" ", "")
    equation = equation.replace("0-", "0s-")
    equation = equation.replace("1-", "1s-")
    equation = equation.replace("2-", "2s-")
    equation = equation.replace("3-", "3s-")
    equation = equation.replace("4-", "4s-")
    equation = equation.replace("5-", "5s-")
    equation = equation.replace("6-", "6s-")
    equation = equation.replace("7-", "7s-")
    equation = equation.replace("8-", "8s-")
    equation = equation.replace("9-", "9s-")
    equation = equation.replace("x-", "xs-")
    equation = equation.replace("^2", "")
    equation = equation.replace("^", "")
    equation = equation.replace("x", "")
    num0, num1, num2 = equation.split("s")

